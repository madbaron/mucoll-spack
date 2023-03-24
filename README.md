# [Spack](https://github.com/spack/spack) package repository for Muon Collider software stack

This repository holds a set of Spack recipes for Muon Collider software (under namespace `mucoll`) based on [Key4hep](https://key4hep.github.io/key4hep-doc/) stack. It extends the corresponding [key4hep-stack](https://github.com/key4hep/key4hep-spack) repository, which is required for installation, overriding several packages by the ones customised for Muon Collider simulation studies.

After installing [Spack](https://github.com/key4hep/spack) and downloading the [key4hep-spack](https://github.com/key4hep/key4hep-spack) and [mucoll-spack](https://github.com/MuonColliderSoft/mucoll-spack) repositories, the whole software stack can be installed using the following commands:

```bash
# Add repositories
spack repo add ./key4hep-spack
spack repo add ./mucoll-spack

# Create a Spack environment
spack env create sim
spack env activate sim

# Copy package configurations
cp ./mucoll-spack/environments/mucoll-release/packages.yaml $SPACK_ENV/

# Install the software stack
spack add mucoll-stack
spack concretize
spack install --fail-fast

# Load packages into environment
spack load
```

## Package versioning

Preferred convention for version names in Spack is numbers separated by dots, without leading zeros, e.g. `1.2.13`.
Conversion to tag names in `mucoll` packages is provided by `MCIlcsoftpackage` class defined in `packages/mucoll-stack/mucoll_utils.py`, e.g. for [`lcgeo`](https://github.com/MuonColliderSoft/lcgeo/releases/tag/v00-17-MC) package version `0.17` corresponds to tag name `v00-17-MC`.


## Adding new versions for individual packages

After a new tag for repository is created, e.g. `v00-17-MC` in `lcgeo` repository, it can be added to this Spack repository in two steps:

1. Get the archive checksum for the new tag
```bash
spack checksum lcgeo 0.17
# Validates archive URL and returns the checksum
    version('0.17', sha256='5ab33aaf5bc37deba82c2dde78cdce6c0041257222ed7ea052ecdd388a41cf9b')
```

2. Add the returned version definition to the corresponding package file: [`packages/lcgeo/package.py`](packages/lcgeo/package.py)

> NOTE: This repository only contains packages maintained by the Muon Collider collaboration.
> If the version of interest is missing from Spack for an external package, the line with new version definition should be added to the package file in the corresponding repository.
> To see locations of other repositories: `spack repo list`

