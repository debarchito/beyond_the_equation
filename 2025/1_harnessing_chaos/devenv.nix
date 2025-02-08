{ pkgs, ... }:

{
  languages.julia = {
    enable = true;
    package = pkgs.julia_111;
  };
}
