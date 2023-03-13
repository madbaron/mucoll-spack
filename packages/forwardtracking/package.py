# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Forwardtracking(CMakePackage, Ilcsoftpackage):
    """Track Reconstruction for the Forward Direction (for the FTD)"""

    homepage = "https://github.com/MuonColliderSoft/ForwardTracking"
    git      = "https://github.com/MuonColliderSoft/ForwardTracking.git"
    url      = "https://github.com/MuonColliderSoft/ForwardTracking/archive/refs/tags/v01-14-mucoll-01.tar.gz"

    maintainers = ['gianelle', 'pandreetto']

    version('master', branch='master')
    version('1.14.1', sha256='d5d6a34730b2024022d4f57a5f250e508b53cae2')

    patch('testing.patch', when="@:1.15")

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('root')
    depends_on('clhep')
    depends_on('raida')

    def cmake_args(self):
        args = []
        args.append(self.define('BUILD_TESTING', self.run_tests))
        args.append(self.define('CMAKE_CXX_STANDARD',
                                self.spec['root'].variants['cxxstd'].value))
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libForwardTracking.so")
