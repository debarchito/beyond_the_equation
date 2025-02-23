## 1. Setup

- If you have [direnv](https://direnv.net/) installed, you can just run
  `direnv allow` and the project should scaffold itself with the proper version
  of [Julia](https://julialang.org/) (which is `1.11.x`).
- Alternatively, you can use a package manager of your choice or download the
  binaries from
  [https://julialang.org/downloads](https://julialang.org/downloads/).
- Another option is to use [juliaup](https://github.com/JuliaLang/juliaup/), a version
  multiplexer for **Julia**. This method is recommended for most users.

## 2. Run

> `NOTE:` If you have [just](https://github.com/casey/just) installed, you can
> run the project using the following command:
>
> ```sh
> just
> ```
> For **direnv** users, **just** is installed automatically.

```sh
❯ julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.11.3 (2025-01-21)
 _/ |\__'_|_|_|\__'_|  |
|__/                   |

julia> # Tap `]` to enter the package manager
(@v1.11) pkg> activate . # Activate the env
(HarnessingChaos) pkg> instantiate # To install the dependencies
(HarnessingChaos) pkg> # Tap `backspace` to exit the package manager
julia> using Pluto
julia> Pluto.run()
```

In the **Pluto.jl UI**, select the [src/HarnessingChaosPluto.jl](src/HarnessingChaosPluto.jl) notebook to start working with the interactive environment.

Please note that the [src/HarnessingChaos.jl](src/HarnessingChaos.jl) file is intentionally left as an empty module. This is to prevent **Julia** from raising any precompilation errors during initialization.

## 3. Licensing

The code samples are licensed under the [MIT](../../LICENSE-MIT) License, while the materials are made available in the public domain under the [CC0 1.0 Universal](../../LICENSE-CC0) license.
