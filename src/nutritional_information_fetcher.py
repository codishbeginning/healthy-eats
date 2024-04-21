import requests

""" This class defines methods that fetch nutritional information"""

class NutritionalInformationFetcher:
    """ This class defines methods that fetch nutritional information"""

    def __init__(self):
        pass

    def fetch_nutritional_information(self,barcode):
        """ This method fetches nutritional information from Open food facts API"""
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url)
        
        """Check If response from the api is successful"""
        if response.status_code == 200:
            data = response.json()
            product = data.get('product')
            """Check if product object is valid"""
            if product:
                print()
                print("**************Product information***************")
                product_name = product.get('product_name', 'N/A')
                pnns_groups_1 = product.get('pnns_groups_1', 'N/A')
                pnns_groups_1_tags = product.get('pnns_groups_1_tags', {})

                print(f"Product Name: {product_name}")
                print(f"Product Tags: {pnns_groups_1_tags}")
                print(f"Product Type: {pnns_groups_1}")

                print()

                print("**************Nutritional information***************")
                nutrients = product.get('nutriments', {})

                fat = nutrients.get('fat', 'N/A')
                fat_unit = nutrients.get('fat_unit', 'N/A')
                saturated_fat = nutrients.get('saturated-fat', 'N/A')
                saturated_fat_unit = nutrients.get('saturated-fat_unit', 'N/A')
                sodium = nutrients.get('sodium', 'N/A')
                sodium_unit = nutrients.get('sodium_unit', 'N/A')
                carbohydrates = nutrients.get('carbohydrates', 'N/A')
                carbohydrates_unit = nutrients.get('carbohydrates_unit', 'N/A')
                sugars = nutrients.get('sugars', 'N/A')
                sugars_unit = nutrients.get('sugars_unit', 'N/A')
                proteins = nutrients.get('proteins', 'N/A')
                proteins_unit = nutrients.get('proteins_unit', 'N/A')

                nutriscore_data = product.get('nutriscore_data', {})
                fiber_value = nutriscore_data.get('fiber_value','N/A')

                print(f"Fats: {fat} {fat_unit}")
                print(f"   Saturated Fat: {saturated_fat} {saturated_fat_unit}")
                print(f"Sodium: {sodium} {sodium_unit}")
                print(f"Carbohydrates: {carbohydrates} {carbohydrates_unit}")
                print(f"   Dietary Fiber: {fiber_value}")
                print(f"   Sugars: {sugars} {sugars_unit}")
                print(f"Proteins: {proteins} {proteins_unit}")


                print()
            else:
                print("Product not found for barcode " + barcode)
        else:
            print("Failed to get nutritional data")

        return True
    
    def is_suitable_for_diabetics(self, ingredients_list: list):
        """ This method helps determine if the food is suitable for a diabetic patient""" 
        return True
    

nutritionalInfo = NutritionalInformationFetcher()
nutritionalInfo.fetch_nutritional_information("3017624010701")
"""nutritionalInfo.fetch_nutritional_information("737628064502")"""
