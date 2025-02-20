## 1. Setup

- If you have [direnv](https://direnv.net/) configured, you can just run
  `direnv allow` and the project should scaffold itself with the proper version
  of [Julia](https://julialang.org/) (which is `1.11.x`).
- Alternatively, you can use a package manager of your choice or download the
  binaries from
  [https://julialang.org/downloads](https://julialang.org/downloads/). You can
  also use [juliaup](https://github.com/JuliaLang/juliaup/) which is a version
  multiplexer for **Julia**.

## 2. Run

```sh
❯ julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.11.x (2025-01-21)
 _/ |\__'_|_|_|\__'_|  |
|__/                   |

julia> # Tap `]` to enter the package manager
(@v1.11) pkg> activate . # Activate the env
(HarnessingChaos) pkg> instantiate # To install Pluto.jl
(HarnessingChaos) pkg> # Tap `backspace` to exit the package manager
julia> using Pluto
julia> Pluto.run()
```

In the **Pluto** UI, choose the
[src/HarnessingChaosPluto.jl](src/HarnessingChaosPluto.jl) file to start the
notebook.

## 3. Licensing

This project is licensed under the [MIT](../../LICENSE-MIT) license.
