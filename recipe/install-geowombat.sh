#!/bin/bash
set -ex

# For cross-compilation, pass meson args (including --cross-file) through pip
if [[ "${CONDA_BUILD_CROSS_COMPILATION:-}" == "1" ]]; then
  ${PYTHON} -m pip install . -vv --no-deps --no-build-isolation \
    -Csetup-args=${MESON_ARGS// / -Csetup-args=}
else
  ${PYTHON} -m pip install . -vv --no-deps --no-build-isolation
fi
