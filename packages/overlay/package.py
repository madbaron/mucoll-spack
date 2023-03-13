# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Overlay(CMakePackage, Ilcsoftpackage):
    """The package Overlay provides code for event overlay with Marlin."""

    homepage = "https://github.com/MuonColliderSoft/Overlay"
    git      = "https://github.com/MuonColliderSoft/Overlay.git"
    url      = "https://github.com/iLCSoft/Overlay/archive/v00-22.tar.gz"

    maintainers = ['gianelle', 'pandreetto']

    version('master', branch='master')
    version('0.24',   sha256='https://github.com/MuonColliderSoft/Overlay/commit/e1cf5d283293fecbf20da89e925707f01a2a1eff')
    version('0.23',   sha256='https://github.com/MuonColliderSoft/Overlay/commit/e581bd5d37e4da09373200c0628f86c6785e3040')
    version('0.22',   sha256='https://github.com/MuonColliderSoft/Overlay/commit/c6f6501dbff4aa0873e0a55ef7709208b8f471e4')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('clhep')
    depends_on('raida')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libOverlay.so")

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
