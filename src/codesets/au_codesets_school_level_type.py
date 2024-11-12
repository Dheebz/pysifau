

from enum import Enum


class AUCodeSetsSchoolLevelType:
    code:str
    class SchoolLevelTypeEnums(Enum):
        CAMP = "Camp"
        COMMTY = "Commty"
        EARLYCH = "EarlyCh"
        JUNPRI = "JunPri"
        KGARTEN = "Kgarten"
        KIND = "Kind"
        LANG = "Lang"
        MCH = "MCH"
        OTHER = "Other"
        PRESCH = "PreSch"
        PRISEC = "Pri/Sec"
        PRI = "Pri"
        SEC = "Sec"
        SENIOR = "Senior"
        SPECP12 = "Spec/P-12"
        SPECPRI = "Spec/Pri"
        SPECSEC = "Spec/Sec"
        SPECIAL = "Special"
        SPECIALASSISTANCE = "SpecialAssisstance"
        SPECIF = "Specif"
        SUPP = "Supp"
        UNKNOWN = "Unknown"

    def __post_init__(self):
        if self.code not in [item.value for item in self.SchoolLevelTypeEnums]:
            raise ValueError(f"{self.code} is not a valid school level type")
        
    def __str__(self):
        return self.code
    
    def __repr__(self):
        return f"AUCodeSetsSchoolLevelType(code='{self.code}')"
    
    def __eq__(self,other:"AUCodeSetsSchoolLevelType"):
        
