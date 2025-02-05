{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    package = pkgs.python313;
    uv.enable = true;
    uv.sync.enable = true;
    venv.enable = true;
  };
  packages = with pkgs; [
    cairo
    pango
    texliveFull
  ];
  enterShell = ''
    uv venv
    uv sync
  '';
}
