class details():
	#use  pdbopdbqt.pdb.value(filename,variable)
	def __init__(self):
		print ("use  pdbopdbqt.pdb.value(filename,variable)")
	def covalent_radius():
		return {"H":"53","Li":"167","Na":"190","K":"243","Rb":"265","Cs":"298","La":"226","Be":"112","Mg":"145","Ca":"194",
	"Sr":"219","Ba":"253","Ce":"210","Sc":"184","Y":"212","Pr":"247","Ti":"176","Zr":"206","Hf":"208","Nd":"206","V":"171","Nb":"198","Ta":"200","Pm":"205","Cr":"166","Mo":"190",
	"W":"193","Sm":"238","Mn":"161","Tc":"183","Re":"188","Eu":"231","Fe":"156","Ru":"178","Os":"185","Gd":"233","Co":"152","Rh":"173",
	"Ir":"180","Tb":"225","Ni":"149","Pd":"169","Pt":"177","Dy":"228","Cu":"145","Ag":"165","Au":"174","Ho":"226","Zn":"142","Cd":"161","Hg":"171","Er":"226","B":"87","Al":"118",
	"Ga":"136","In":"156","Tl":"156","Tm":"222","C":"67","Si":"111","Ge":"125","Sn":"145","Pb":"154","Yb":"222","N":"56","P":"98","As":"114","Sb":"133","Bi":"143","Lu":"217",
	"O":"48","S":"88","Se":"103","Te":"123","Po":"135","F":"42","Cl":"79","Br":"94","I":"115","At":"127","He":"31","Ne":"38","Ar":"71","Kr":"88","Xe":"108","Rn":"120"}
	
	def atom_type(atom_type):
		atoms = {"Br":"Br","C":"C","CA":"C","CB":"C","CC":"C","CK":"C","CM":"C","CN":"C","CQ":"C","CR":"C","CT":"C","CV":"C","CW":"C","CG":"C","CH":"C","CD":"C","CZ":"C","CE":"C","SD":"S","C*":"C","C0":"Ca","F":"F","H":"H","HC":"H","H1":"H","H2":"H","H3":"H","HA":"H","HB":"H","HH":"H","HD":"H","HZ":"H","HG":"H","HE":"H","H4":"H","H5":"H","HO":"H","HS":"H","HW":"H","HP":"H","I":"I","Cl":"Cl","Na":"Na","MG":"Mg","N":"N","NE":"N","NZ":"N","NH":"N","N":"N","NB":"N","NC":"N","N2":"N","N3":"N","N*":"N","ND":"N","O":"O","OD":"O","OW":"O","OH":"O","OE":"O","OS":"O","OXT":"O","OG":"O","O2":"O","P":"P","S":"S","SH":"S","SG":"S","CU":"Cu","FE":"Fe","K":"K","Rb":"Rb","Cs":"Cs","OW_spc":"O","HW_spc":"H","Li":"Li","Zn":"Zn"}
		atom_name = ""
		for letters in atom_type:
			if not letters.isdigit():
				atom_name += letters
		return (atoms[atom_name])
		
	def van_radius():
		return {'H':'120',"Fe": "219",	'Zn':'139',	'He':'140',	'Cu':'140',	'Fl':'147',	'O':'152',	'Ne':'154',	'N':'155',	'Hg':'155',	'Cd':'158',
		'Ag':'172',	'Mg':'173',	'Cl':'175',	'Pt':'175',	'P':'180',	'S':'180',	'Li':'182',	'As':'185',	'Br':'185',	'U':'186',
		'Ti':'196',	'I':'198',	'Kr':'202',	'Pb':'202',	'Te':'206',	'Si':'210',	'Xe':'216',	'Sn':'217',	'Na':'227',	'K':'275',
		'Ni':'163',	'Pd':'163',	'Au':'166',	'C':'170',	'Ga':'187',	'Ar':'188',	'Se':'190',	'In':'193'}
	def mass():
		return {'H':'1.00794','O':'15.999','N':'14.0067','S':'32.065','C':'12.0107','P':'30.973762 '}