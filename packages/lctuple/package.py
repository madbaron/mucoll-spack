# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lctuple(CMakePackage, Ilcsoftpackage):
    """Marlin package that creates a ROOT TTree with a column wise ntuple from LCIO collections."""

    homepage = "https://github.com/MuonColliderSoft/LCTuple"
    git      = "https://github.com/MuonColliderSoft/LCTuple.git"
    url      = "https://github.com/MuonColliderSoft/LCTuple/archive/refs/tags/v01-15-MC.tar.gz"

    maintainers = ['gianelle', 'pandreetto']

    version('master', branch='master')
    version('1.15',   sha256='742e9849929d80485f8d2da22a50a7c98f61adaf')
    version('1.14',   sha256='1d56e1ffe59ed24f890cd412d5fa7c2026f67702')
    version('1.13',   sha256='d53cc628b7efe48f1282f9655872aaa27c85d380')
    version('1.12',   sha256='aa9289efcf0b936e8a6613a008cda8ab8d7eb5d3')


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libLCTuple.so")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args
