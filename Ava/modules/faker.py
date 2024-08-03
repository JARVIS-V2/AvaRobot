import random
from faker import Faker
from pyrogram import filters
from Ava import Jarvis as app

# Initialize Faker
fake = Faker()


def get_faker_locale(country_code):
    # Get Faker locale based on country code or default to 'en_US'
    return fake.locales.get(country_code, "en_US")

def generate_fake_address(country_code="us"):
    # Check if country code is valid
    if country_code not in COUNTRY_CODES:
        return {"Error": "Country code not found"}

    fake_locale = get_faker_locale(country_code)
    faker = Faker(locale=fake_locale)
    country_name = COUNTRY_CODES.get(country_code, "Unknown Country")

    # Fallback values
    state = getattr(faker, 'state', lambda: "N/A")()
    province = getattr(faker, 'province', lambda: "N/A")()
    region = getattr(faker, 'region', lambda: "N/A")()
    formatted_state = next((x for x in [state, province, region] if x != "N/A"), "N/A")

    city = getattr(faker, 'city', lambda: "N/A")()
    town = getattr(faker, 'town', lambda: "N/A")()
    village = getattr(faker, 'village', lambda: "N/A")()
    formatted_city = next((x for x in [city, town, village] if x != "N/A"), "N/A")

    street_address = getattr(faker, 'street_address', lambda: "N/A")()
    postcode = getattr(faker, 'postcode', lambda: "N/A")()
    email = getattr(faker, 'email', lambda: "N/A")()
    if "example" in email:
        email = email.replace("example.com", random.choice(["yahoo.com", "gmail.com", "outlook.com"]))\
                     .replace("example.org", random.choice(["yahoo.com", "gmail.com", "outlook.com"]))\
                     .replace("example.net", random.choice(["yahoo.com", "gmail.com", "outlook.com"])).lower()

    return {
        "Name": faker.name(),
        "Gender": faker.random_element(elements=('Male', 'Female')),
        "Street Address": street_address,
        "City/Town/Village": formatted_city,
        "State/Province/Region": formatted_state,
        "Pincode": postcode,
        "Country": country_name,
        "Mobile Number": f"+{faker.phone_number()}",
        "Email": email,
    }

def format_address_details(address_details):
    if "Error" in address_details:
        return f"**Error**: {address_details['Error']}"
    
    response = [f"**{address_details['Country']} Address Generated** ✅", "", "▰▰▰▰▰▰▰▰▰▰▰▰▰"]
    for key, value in address_details.items():
        response.append(f"•➥ **{key}**: `{value}`")
    return "\n".join(response)

@app.on_message(filters.command(["fake"], prefixes=[".", "/"]))
async def send_fake_address_details(client, message):
    command_text = message.text.split()
    country_code = command_text[1] if len(command_text) > 1 and command_text[1] in COUNTRY_CODES else "us"
    address_details = generate_fake_address(country_code)
    formatted_details = format_address_details(address_details)
    await client.send_message(message.chat.id, formatted_details)
