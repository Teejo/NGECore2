import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('master_prophet_of_the_dark_side')
	mobileTemplate.setLevel(80)
	mobileTemplate.setDifficulty(1)
	mobileTemplate.setAttackRange(15)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(9)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("imperial")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("imperial")
	mobileTemplate.setFactionStatus(1)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_female_human_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_female_human_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_female_human_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_male_human_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_male_human_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_male_human_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_elder_male_human_04.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/sword/crafted_saber/shared_sword_lightsaber_one_handed_gcw_s01_gen4.iff', 9, 1.0)
	weapontemplate = WeaponTemplate('object/weapon/melee/sword/crafted_saber/shared_sword_lightsaber_one_handed_gcw_s01_gen5.iff', 9, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('saberhit')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('master_prophet_dark_side', mobileTemplate)
	return