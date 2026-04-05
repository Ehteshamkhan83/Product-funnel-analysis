import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("Data/events.csv")

# print("First 5 rows:")
# print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nEvent types:")
print(df['event_type'].value_counts())

# Funnel analysis
funnel = df.groupby('event_type')['user_id'].nunique()
print("\nUsers at each stage:")
print(funnel)

view_users = funnel.get('view',0)
cart_users = funnel.get('cart',0)
purchase_users = funnel.get('purchase',0)

print("\nView users:", view_users)
print("Cart users:", cart_users)
print("Purchase users:", purchase_users)

# stages = ['View','Cart','Purchase']
# values = [view_users,cart_users,purchase_users]
#
# plt.bar(stages,values)
# plt.title("Product Funnel")
# plt.savefig("funnel_chart.png")
# plt.show()

view_users = funnel.get('view',0)
cart_users = funnel.get('cart',0)
purchase_users = funnel.get('purchase',0)

view_to_cart = cart_users / view_users
cart_to_purchase = purchase_users / cart_users

print("\nView → Cart Conversion:", view_to_cart)
print("Cart → Purchase Conversion:", cart_to_purchase)

drop_view_cart = (view_users - cart_users) / view_users
drop_cart_purchase = (cart_users - purchase_users) / cart_users

print("\nDrop View → Cart:", drop_view_cart)
print("Drop Cart → Purchase:", drop_cart_purchase)

top_products = df[df['event_type'] == 'purchase']['product_id'].value_counts().head(10)

print("\nTop 10 Selling Products:")
print(top_products)

top_viewed = df[df['event_type'] == 'view']['product_id'].value_counts().head(10)

print("\nMost Viewed Products:")
print(top_viewed)

top_revenue_products = (
    df[df['event_type'] == 'purchase']
    .groupby('product_id')['price']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Revenue Products:")
print(top_revenue_products)

top_categories = (
    df[df['event_type'] == 'purchase']
    .groupby('category_code')['price']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Categories by Revenue:")
print(top_categories)




















