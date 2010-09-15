import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(0.05),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(7000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         crossSection  = cms.untracked.double(0.18),
                         PythiaParameters = cms.PSet(pythiaUESettingsBlock,
                                                     processParameters = cms.vstring('PMAS(5,1)= 4.8         ! b quark mass',
                                                                                     'PMAS(6,1)= 175.0       ! t quark mass',
                                                                                     'PMAS(347,1)= 750.0     ! mass of RS Graviton',
                                                                                     'PARP(50) = 0.27        ! 0.054 == c=0.01 (k/M_PL=0.01)',
                                                                                     'MSEL=0                 ! (D=1) 0 to select full user control',
                                                                                     'MSUB(391)=1               ! q qbar -> G* ',
                                                                                     'MSUB(392)=1               ! g g -> G*',
                                                                                     '5000039:ALLOFF            ! Turn off all decays of G*',
                                                                                     '5000039:ONIFANY 23        ! Turn on the decays ZZ'),
                                                     parameterSets = cms.vstring('pythiaUESettings',
                                                                                 'processParameters')
                                                     )
                         )

eejjFilter  = cms.EDFilter("TwoVBGenFilter",
    src      = cms.untracked.InputTag("generator"),
    eejj     = cms.bool(True),
    enujj    = cms.bool(False),
    mumujj   = cms.bool(False),
    munujj   = cms.bool(False),
    tautaujj = cms.bool(False),
    taunujj  = cms.bool(False),
    nunujj   = cms.bool(False)
)

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.3 $'),
        name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_EXOTICA_RSGravZZ_kMpl005_M750_7TeV_eejj_cff.py,v $'),
        annotation = cms.untracked.string('default documentation string for PYTHIA6_EXOTICA_RSGravZZ_kMpl005_M750_7TeV_eejj_cff.py')
)

ProductionFilterSequence = cms.Sequence(generator*eejjFilter)