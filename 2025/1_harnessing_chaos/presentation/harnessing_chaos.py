import random
import numpy as np
from manim import Scene, Dot, Text, Line
from manim import rate_functions, smooth, FadeIn
from manim import WHITE, GRAY_A, GRAY_B, GRAY_C, GRAY_D, BLUE, PURPLE
from manim import DOWN, LEFT, RIGHT, UP
from manim.opengl import OpenGLVGroup


class HarnessingChaos(Scene):
    def construct(self):
        num_particles = 1200
        particles = OpenGLVGroup(
            *[
                Dot(
                    radius=0.04,
                    color=random.choice([WHITE, GRAY_A, GRAY_B, GRAY_C, GRAY_D]),
                ).move_to(
                    np.array([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
                )
                for _ in range(num_particles)
            ]
        )

        self.add(particles)

        def chaotic_movement(mob, dt):
            for p in mob:
                p.shift(np.random.uniform(-1, 1, 3) * dt)

        particles.add_updater(chaotic_movement)

        self.wait(1.5)

        wave = Line(start=LEFT * 7, end=RIGHT * 7, stroke_width=0).move_to(LEFT * 7)
        self.play(wave.animate.shift(RIGHT * 14), run_time=2, rate_func=smooth)

        target_text = Text("Harnessing Chaos!", font_size=72, gradient=(BLUE, PURPLE))
        target_points = target_text.get_all_points()[:num_particles]

        self.play(
            *[
                p.animate.move_to(target_points[i])
                for i, p in enumerate(particles[: len(target_points)])
            ],
            run_time=1.5,
            rate_func=rate_functions.ease_out_cubic,
        )

        self.play(
            *[p.animate.set_opacity(0) for p in particles],
            FadeIn(target_text),
            run_time=1,
        )

        subtitle = Text("beyond_the_equation - 1", font_size=32, color=GRAY_C)
        subtitle.next_to(target_text, DOWN)

        self.play(FadeIn(subtitle, shift=UP * 0.5), run_time=1.2)

        self.wait(2)
        self.interactive_embed()
