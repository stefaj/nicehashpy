with import <nixpkgs> {};
with pkgs.python27Packages;

buildPythonPackage{
    name = "nicehash";
    buildInputs = [ 
                    python27Full
                    python27Packages.requests
                    python27Packages.setuptools
                    python27Packages.numpy
                   ]; 
  shellHook = ''
  # set SOURCE_DATE_EPOCH so that we can use python wheels
  SOURCE_DATE_EPOCH=$(date +%s)
  CPATH=$CPATH:~/.local/include
  LIBRARY_PATH=$LIBRARY_PATH:~/.local/lib
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.local/lib
  '';

}

