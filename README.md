# [Spack](https://github.com/spack/spack) package repository for Muon Collider software stack

This repository holds a set of Spack recipes for Muon Collider software (under namespace `mucoll`) based on [Key4hep](https://key4hep.github.io/key4hep-doc/) stack. It extends the corresponding [key4hep-stack](https://github.com/key4hep/key4hep-spack) repository, which is required for installation, overriding several packages by the ones customised for Muon Collider simulation studies.

After installing [Spack](https://github.com/key4hep/spack) and downloading the [key4hep-spack](https://github.com/key4hep/key4hep-spack) and [mucoll-spack](https://github.com/MuonColliderSoft/mucoll-spack) repositories, the whole software stack can be installed using the following commands:

```bash
# Add repositories
spack repo add key4hep-spack
spack repo add mucoll-spack

# Create a Spack environment
spack env create sim
spack env activate sim

# Copy package configurations
cp mucoll-spack/environments/mucoll-common/packages.yaml $SPACK_ENV/

# Install the software stack
spack add mucoll-stack
spack concretize
spack install --fail-fast
```
