from dotenv import load_dotenv
from datetime import date
from notion.client import NotionClient
from notion.block import *

load_dotenv()

client = NotionClient(token_v2=os.getenv("token"))
recurring_table = client.get_collection_view(os.getenv("recurring_url"))
bujo_page = client.get_block(os.getenv("bujo_url"))

# for row in recurring_table.collection.get_rows():
#     print("Item '{}' has type {} with info {}".format(row.name, row.recurrence_type, row.recurrence_info))

current_date = date.today()

# get list of all years in bujo
year_list = []
for child in bujo_page.children:
    year_list.append(child.title)

if current_date.year not in year_list:
    year_page = bujo_page.children.add_new(PageBlock, title=current_date.year)
# month_page = year_page.children.add_new(PageBlock, title="January")
# week_page = month_page.children.add_new(PageBlock, title="Week 2")



