import random
import string
from faker import Faker
from pyrogram import filters
from Ava import Jarvis as app

# Mapping of country codes to country names and their corresponding phone codes
COUNTRY_CODES = {
    "ad": "Andorra", "ae": "United Arab Emirates", "af": "Afghanistan",
    "ag": "Antigua and Barbuda", "ai": "Anguilla", "al": "Albania",
    "am": "Armenia", "ao": "Angola", "aq": "Antarctica", "ar": "Argentina",
    "as": "American Samoa", "at": "Austria", "au": "Australia", "aw": "Aruba",
    "ax": "Åland Islands", "az": "Azerbaijan", "ba": "Bosnia and Herzegovina",
    "bb": "Barbados", "bd": "Bangladesh", "be": "Belgium", "bf": "Burkina Faso",
    "bg": "Bulgaria", "bh": "Bahrain", "bi": "Burundi", "bj": "Benin",
    "bl": "Saint Barthélemy", "bm": "Bermuda", "bn": "Brunei Darussalam",
    "bo": "Bolivia", "bq": "Bonaire, Sint Eustatius and Saba", "br": "Brazil",
    "bs": "Bahamas", "bt": "Bhutan", "bv": "Bouvet Island", "bw": "Botswana",
    "by": "Belarus", "bz": "Belize", "ca": "Canada", "cc": "Cocos (Keeling) Islands",
    "cd": "Congo, Democratic Republic of the", "cf": "Central African Republic",
    "cg": "Congo", "ch": "Switzerland", "ci": "Côte d'Ivoire", "ck": "Cook Islands",
    "cl": "Chile", "cm": "Cameroon", "cn": "China", "co": "Colombia",
    "cr": "Costa Rica", "cu": "Cuba", "cv": "Cabo Verde", "cw": "Curaçao",
    "cx": "Christmas Island", "cy": "Cyprus", "cz": "Czechia", "de": "Germany",
    "dj": "Djibouti", "dk": "Denmark", "dm": "Dominica", "do": "Dominican Republic",
    "dz": "Algeria", "ec": "Ecuador", "ee": "Estonia", "eg": "Egypt",
    "eh": "Western Sahara", "er": "Eritrea", "es": "Spain", "et": "Ethiopia",
    "fi": "Finland", "fj": "Fiji", "fm": "Micronesia", "fo": "Faroe Islands",
    "fr": "France", "ga": "Gabon", "gb": "United Kingdom", "gd": "Grenada",
    "ge": "Georgia", "gf": "French Guiana", "gg": "Guernsey", "gh": "Ghana",
    "gi": "Gibraltar", "gl": "Greenland", "gm": "Gambia", "gn": "Guinea",
    "gp": "Guadeloupe", "gq": "Equatorial Guinea", "gr": "Greece", "gt": "Guatemala",
    "gu": "Guam", "gw": "Guinea-Bissau", "gy": "Guyana", "hk": "Hong Kong",
    "hm": "Heard Island and McDonald Islands", "hn": "Honduras", "hr": "Croatia",
    "ht": "Haiti", "hu": "Hungary", "id": "Indonesia", "ie": "Ireland", "il": "Israel",
    "im": "Isle of Man", "in": "India", "io": "British Indian Ocean Territory", "iq": "Iraq",
    "ir": "Iran", "is": "Iceland", "it": "Italy", "je": "Jersey", "jm": "Jamaica",
    "jn": "Jinmen", "jo": "Jordan", "jp": "Japan", "ke": "Kenya", "kg": "Kyrgyzstan",
    "kh": "Cambodia", "ki": "Kiribati", "km": "Comoros", "kn": "Saint Kitts and Nevis",
    "kp": "North Korea", "kr": "South Korea", "kw": "Kuwait", "ky": "Cayman Islands",
    "kz": "Kazakhstan", "la": "Lao People's Democratic Republic", "lb": "Lebanon",
    "lc": "Saint Lucia", "li": "Liechtenstein", "lk": "Sri Lanka", "lr": "Liberia",
    "ls": "Lesotho", "lt": "Lithuania", "lu": "Luxembourg", "lv": "Latvia", "ly": "Libya",
    "ma": "Morocco", "mc": "Monaco", "md": "Moldova", "me": "Montenegro",
    "mf": "Saint Martin", "mg": "Madagascar", "mh": "Marshall Islands", "mk": "North Macedonia",
    "ml": "Mali", "mm": "Myanmar", "mn": "Mongolia", "mo": "Macao", "mp": "Northern Mariana Islands",
    "mq": "Martinique", "mr": "Mauritania", "ms": "Montserrat", "mt": "Malta", "mu": "Mauritius",
    "mv": "Maldives", "mw": "Malawi", "mx": "Mexico", "my": "Malaysia", "mz": "Mozambique",
    "na": "Namibia", "nc": "New Caledonia", "ne": "Niger", "nf": "Norfolk Island",
    "ng": "Nigeria", "ni": "Nicaragua", "nl": "Netherlands", "no": "Norway", "np": "Nepal",
    "nr": "Nauru", "nu": "Niue", "nz": "New Zealand", "om": "Oman", "pa": "Panama",
    "pe": "Peru", "pf": "French Polynesia", "pg": "Papua New Guinea", "ph": "Philippines",
    "pk": "Pakistan", "pl": "Poland", "pm": "Saint Pierre and Miquelon", "pn": "Pitcairn",
    "pr": "Puerto Rico", "pt": "Portugal", "pw": "Palau", "py": "Paraguay", "qa": "Qatar",
    "re": "Réunion", "ro": "Romania", "rs": "Serbia", "ru": "Russia", "rw": "Rwanda",
    "sa": "Saudi Arabia", "sb": "Solomon Islands", "sc": "Seychelles", "sd": "Sudan",
    "se": "Sweden", "sg": "Singapore", "sh": "Saint Helena", "si": "Slovenia",
    "sj": "Svalbard and Jan Mayen", "sk": "Slovakia", "sl": "Sierra Leone", "sm": "San Marino",
    "sn": "Senegal", "so": "Somalia", "sr": "Suriname", "ss": "South Sudan",
    "st": "São Tomé and Príncipe", "sv": "El Salvador", "sx": "Sint Maarten",
    "sy": "Syria", "sz": "Eswatini", "tc": "Turks and Caicos Islands", "td": "Chad",
    "tf": "French Southern Territories", "tg": "Togo", "th": "Thailand", "tj": "Tajikistan",
    "tk": "Tokelau", "tl": "Timor-Leste", "tm": "Turkmenistan", "tn": "Tunisia",
    "to": "Tonga", "tr": "Turkey", "tt": "Trinidad and Tobago", "tv": "Tuvalu",
    "tz": "Tanzania", "ua": "Ukraine", "ug": "Uganda", "um": "United States Minor Outlying Islands",
    "us": "United States", "uy": "Uruguay", "uz": "Uzbekistan", "va": "Vatican City",
    "vc": "Saint Vincent and the Grenadines", "ve": "Venezuela", "vg": "British Virgin Islands",
    "vi": "U.S. Virgin Islands", "vn": "Vietnam", "vu": "Vanuatu", "wf": "Wallis and Futuna",
    "ws": "Samoa", "xk": "Kosovo", "ye": "Yemen", "yt": "Mayotte", "za": "South Africa",
    "zm": "Zambia", "zw": "Zimbabwe"
}

FAKER_LOCALES = {
    "ad": "en_US", "ae": "en_AE", "af": "en_AF", "ag": "en_US", "ai": "en_US", "al": "en_US",
    "am": "en_AM", "ao": "en_AO", "aq": "en_US", "ar": "es_AR", "as": "en_US", "at": "de_AT",
    "au": "en_AU", "aw": "en_US", "ax": "sv_SE", "az": "en_AZ", "ba": "en_BA", "bb": "en_US",
    "bd": "en_BD", "be": "nl_BE", "bf": "fr_BF", "bg": "bg_BG", "bh": "en_BH", "bi": "fr_BI",
    "bj": "fr_BJ", "bl": "fr_BL", "bm": "en_US", "bn": "en_BN", "bo": "es_BO", "bq": "en_US",
    "br": "pt_BR", "bs": "en_US", "bt": "en_IN", "bv": "en_US", "bw": "en_BW", "by": "be_BY",
    "bz": "en_BZ", "ca": "en_CA", "cc": "en_AU", "cd": "fr_CD", "cf": "fr_CF", "cg": "fr_CG",
    "ch": "de_CH", "ci": "fr_CI", "ck": "en_CK", "cl": "es_CL", "cm": "en_CM", "cn": "zh_CN",
    "co": "es_CO", "cr": "es_CR", "cu": "es_CU", "cv": "pt_CV", "cw": "en_US", "cx": "en_AU",
    "cy": "en_CY", "cz": "cs_CZ", "de": "de_DE", "dj": "fr_DJ", "dk": "da_DK", "dm": "en_US",
    "do": "es_DO", "dz": "fr_DZ", "ec": "es_EC", "ee": "et_EE", "eg": "ar_EG", "eh": "es_EH",
    "er": "en_ER", "es": "es_ES", "et": "en_ET", "fi": "fi_FI", "fj": "en_FJ", "fm": "en_US",
    "fo": "en_FO", "fr": "fr_FR", "ga": "fr_GA", "gb": "en_GB", "gd": "en_US", "ge": "en_GE",
    "gf": "fr_GF", "gg": "en_GB", "gh": "en_GH", "gi": "en_GI", "gl": "da_GL", "gm": "en_GM",
    "gn": "fr_GN", "gp": "fr_GP", "gq": "es_GQ", "gr": "el_GR", "gt": "es_GT", "gu": "en_US",
    "gw": "pt_GW", "gy": "en_GY", "hk": "zh_HK", "hm": "en_US", "hn": "es_HN", "hr": "hr_HR",
    "ht": "fr_HT", "hu": "hu_HU", "id": "id_ID", "ie": "en_IE", "il": "en_IL", "im": "en_GB",
    "in": "en_IN", "io": "en_US", "iq": "ar_IQ", "ir": "fa_IR", "is": "is_IS", "it": "it_IT",
    "je": "en_GB", "jm": "en_JM", "jn": "zh_TW", "jo": "ar_JO", "jp": "ja_JP", "ke": "en_KE",
    "kg": "en_KG", "kh": "km_KH", "ki": "en_KI", "km": "fr_KM", "kn": "en_US", "kp": "ko_KP",
    "kr": "ko_KR", "kw": "en_KW", "ky": "en_KY", "kz": "kk_KZ", "la": "en_LA", "lb": "ar_LB",
    "lc": "en_LC", "li": "de_LI", "lk": "si_LK", "lr": "en_LR", "ls": "en_LS", "lt": "lt_LT",
    "lu": "lb_LU", "lv": "lv_LV", "ly": "ar_LY", "ma": "ar_MA", "mc": "fr_MC", "md": "ro_MD",
    "me": "en_ME", "mf": "fr_MF", "mg": "fr_MG", "mh": "en_MH", "mk": "mk_MK", "ml": "fr_ML",
    "mm": "my_MM", "mn": "mn_MN", "mo": "zh_MO", "mp": "en_US", "mq": "fr_MQ", "mr": "ar_MR",
    "ms": "en_US", "mt": "en_MT", "mu": "en_MU", "mv": "en_MV", "mw": "en_MW", "mx": "es_MX",
    "my": "ms_MY", "mz": "pt_MZ", "na": "en_NA", "nc": "fr_NC", "ne": "fr_NE", "nf": "en_AU",
    "ng": "en_NG", "ni": "es_NI", "nl": "nl_NL", "no": "no_NO", "np": "ne_NP", "nr": "en_NR",
    "nu": "en_NU", "nz": "en_NZ", "om": "en_OM", "pa": "es_PA", "pe": "es_PE", "pf": "fr_PF",
    "pg": "en_PG", "ph": "en_PH", "pk": "en_PK", "pl": "pl_PL", "pm": "fr_PM", "pn": "en_PN",
    "pr": "en_US", "pt": "pt_PT", "pw": "en_PW", "py": "es_PY", "qa": "ar_QA", "re": "fr_RE",
    "ro": "ro_RO", "rs": "sr_RS", "ru": "ru_RU", "rw": "en_RW", "sa": "ar_SA", "sb": "en_SB",
    "sc": "en_SC", "sd": "ar_SD", "se": "sv_SE", "sg": "en_SG", "sh": "en_SH", "si": "sl_SI",
    "sj": "no_SJ", "sk": "sk_SK", "sl": "en_SL", "sm": "it_SM", "sn": "fr_SN", "so": "en_SO",
    "sr": "nl_SR", "ss": "en_SS", "st": "pt_ST", "sv": "es_SV", "sx": "en_SX", "sy": "ar_SY",
    "sz": "en_SZ", "tc": "en_TC", "td": "fr_TD", "tf": "en_US", "tg": "fr_TG", "th": "th_TH",
    "tj": "tg_TJ", "tk": "en_TK", "tl": "pt_TL", "tm": "en_TM", "tn": "ar_TN", "to": "en_TO",
    "tr": "tr_TR", "tt": "en_TT", "tv": "en_TV", "tz": "en_TZ", "ua": "uk_UA", "ug": "en_UG",
    "um": "en_US", "us": "en_US", "uy": "es_UY", "uz": "en_UZ", "va": "it_VA", "vc": "en_VC",
    "ve": "es_VE", "vg": "en_VG", "vi": "en_VI", "vn": "vi_VN", "vu": "en_VU", "wf": "fr_WF",
    "ws": "en_WS", "xk": "en_XK", "ye": "ar_YE", "yt": "fr_YT", "za": "en_ZA", "zm": "en_ZM",
    "zw": "en_ZW"
}

def generate_fake_passport(country_code="us"):
    fake_locale = FAKER_LOCALES.get(country_code, "en_US")
    fake = Faker(locale=fake_locale)
    country_info = COUNTRY_CODES.get(country_code, ("Unknown Country", ""))
    
    # Generate fake details
    country_name, country_phone_code = country_info
    mobile_number = f"{country_phone_code} {fake.phone_number()}"
    
    # Generate a fake email and replace the domain with 'yahoo.com'
    email = fake.email().replace("example.com", "yahoo.com").lower()
    
    return {
        "Name": fake.name(),
        "Gender": fake.random_element(elements=('Male', 'Female')),
        "Street Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "Pincode": fake.postcode(),
        "Country": country_name,
        "Mobile Number": mobile_number,
        "Email": email,
    }

def format_passport_details(passport_details):
    country = passport_details.get("Country", "Unknown Country")
    response = [
        f"**{country} Address Generated** ✅",
        "", 
        "▰▰▰▰▰▰▰▰▰▰▰▰▰"
    ]
    for key, value in passport_details.items():
        response.append(f"•➥ **{key}**: `{value}`")
    return "\n".join(response)

@app.on_message(filters.command(["fake"], prefixes=[".", "/"]))
async def send_fake_passport_details(client, message):
    command_text = message.text.split()
    country_code = command_text[1] if len(command_text) > 1 and command_text[1] in COUNTRY_CODES else "us"
    passport_details = generate_fake_passport(country_code)
    formatted_details = format_passport_details(passport_details)
    await client.send_message(message.chat.id, formatted_details)
