from .vtigercrm import mapping_vtigercrm
from .ambetter import mapping_ambetter
from .molina import mapping_molina
from .aetna import mapping_aetna
from .healthsherpa import mapping_healthsherpa

mapping_model = {
    "vtigercrm": mapping_vtigercrm,
    "healthsherpa": mapping_healthsherpa,
    "ambetter": mapping_ambetter,
    "molina": mapping_molina,
    "aetna": mapping_aetna,
}

__all__ = ["mapping_model"]
