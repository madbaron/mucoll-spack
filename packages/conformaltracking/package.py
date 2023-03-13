# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Conformaltracking(CMakePackage, Ilcsoftpackage):
    """Package for running pattern recognition based on conformal mapping
       and cellular automaton. This is not tied to a given geometry, but
       has been developed for the CLIC detector model 2015."""

    homepage = "https://github.com/MuonColliderSoft/ConformalTracking"
    git      = "https://github.com/MuonColliderSoft/ConformalTracking.git"
    url      = "https://github.com/MuonColliderSoft/ConformalTracking/archive/refs/tags/v01-11-MC.tar.gz"


    maintainers = ['gianelle', 'pandreetto']

    version('master', branch='master')
    version('1.11',   sha256='5ee8d3062cc2a3ffc68dd14aa8d910283e8af4f5')
    version('1.10',   sha256='c61f9e231f86910685cb647fcd507d55c905e3b6')

    depends_on('ilcutil')
    depends_on('root')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('raida')
    depends_on('boost')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libConformalTracking.so")

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
