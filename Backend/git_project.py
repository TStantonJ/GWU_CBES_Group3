from datetime import datetime
from ontology import all_licenses
license_dictionary = {
"AFL-3.0" : "Academic_Free_License_v3_0",
"Apache-2.0" : "Apache_License_2_0",
"Artistic-2.0" : "Artistic_License_2_0",
"BSD-2-Clause" : "BSD_2_Clause_Simplified_License",
"BSD-3-Clause" : "BSD_3_Clause_Clear_License",
"BSD-4-Clause" : "BSD_4_Clause_Original_or_Old_License",
"0BSD" : "BSD_Zero_Clause_License",
"BSL-1.0" : "Boost_Software_License_1_0",
"CERN-OHL-P-2.0" : "CERN_Open_Hardware_Licence_Version_2_Permissive",
"CERN-OHL-S-2.0" : "CERN_Open_Hardware_Licence_Version_2_Strongly_Reciprocal",
"CERN-OHL-W-2.0" : "CERN_Open_Hardware_Licence_Version_2_Weakly_Reciprocal",
"CECILL-2.1" : "CeCILL_Free_Software_License_Agreement_v2_1",
"CC-BY-4.0" : "Creative_Commons_Attribution_4_0_International",
"CC-BY-SA-4.0" : "Creative_Commons_Attribution_Share_Alike_4_0_International",
"CC0-1.0" : "Creative_Commons_Zero_v1_0_Universal",
"WTFPL" : "Do_What_The_Fuck_You_Want_To_Public_License",
"EPL-1.0" : "Eclipse_Public_License_1_0",
"EPL-2.0" : "Eclipse_Public_License_2_0",
"ECL-2.0" : "Educational_Community_License_v2_0",
"EUPL-1.1" : "European_Union_Public_License_1_1",
"EUPL-1.2" : "European_Union_Public_License_1_2",
"AGPL-3.0" : "GNU_Affero_General_Public_License_v3_0",
"GFDL-1.3" : "GNU_Free_Documentation_License_v1_3",
"GPL-2.0" : "GNU_General_Public_License_v2_0",
"GPL-3.0" : "GNU_General_Public_License_v3_0",
"LGPL-2.1" : "GNU_Lesser_General_Public_License_v2_1",
"LGPL-3.0" : "GNU_Lesser_General_Public_License_v3_0",
"ISC" : "ISC_License",
"LPPL-1.3c" : "LaTeX_Project_Public_License_v1_3c",
"MIT" : "MIT_License",
"MIT-0" : "MIT_No_Attribution",
"MPL-2.0" : "Mozilla_Public_License_2_0",
"MS-PL" : "Microsoft_Public_License",
"MS-RL" : "Microsoft_Reciprocal_License",
"MulanPSL-2.0" : "Mulan_Permissive_Software_License_Version_2",
"ODbL-1.0" : "Open_Data_Commons_Open_Database_License_v1_0",
"OSL-3.0" : "Open_Software_License_3_0",
"PostgreSQL" : "PostgreSQL_License",
"OFL-1.1" : "SIL_Open_Font_License_1_1",
"Unlicense" : "The_Unlicense",
"UPL-1.0" : "Universal_Permissive_License_v1_0",
"NCSA" : "University_of_Illinois__NCSA_Open_Source_License",
"Vim" : "Vim_License",
"Zlib" : "zlib_License"
}

class GitProject:
    def __init__(self, projTitle: str, details: list[str]):
        split_title = projTitle.split('/')
        self.owner = split_title[0]
        self.name = split_title[1]
        self.stars = 0
        self.license = 'MIT_License'
        self.updated = None
        self.lang = 'C'
        
        for detail  in details:
            if parse_stars(detail) > 0:
                self.stars = parse_stars(detail)
            elif detail.startswith('C'):
                self.lang = detail
            elif detail.startswith('Updated'):
                parsed = detail.strip('Updated ')
                reparsed = parsed.strip(',')
                self.updated = datetime.strptime(reparsed, '%b %d, %Y')
            elif len(detail) > 0:
                parsed_license = detail.strip(' license') ## this is formatting from Github

                keyslist = license_dictionary.keys()
                if parsed_license in keyslist:
                    self.license = license_dictionary[parsed_license]
                # for license in all_licenses:
                #     if parsed_license in license:
                #         self.license = license



def parse_stars(starsStr):
    try:
        return int(starsStr)
    except ValueError:
        return 0
