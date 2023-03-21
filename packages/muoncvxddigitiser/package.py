# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.mucoll.mucoll_stack import MCIlcsoftpackage


class Muoncvxddigitiser(CMakePackage, MCIlcsoftpackage):
    """Realistic digitiser of pixelated sensors for Muon Collider"""

    homepage = "https://github.com/MuonColliderSoft/MuonCVXDDigitiser"
    git      = "https://github.com/MuonColliderSoft/MuonCVXDDigitiser.git"

    version('master',  branch='master')
    

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('lcio')
    depends_on('clhep')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMuonCVXDDigitiser.so")

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
