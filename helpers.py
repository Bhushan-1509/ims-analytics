import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import io

def generate_orders_pie_chart(df):
    # Count the number of completed and pending orders
    completed_count = df[df['status'] == 1].shape[0]
    pending_count = df[df['status'] == 0].shape[0]
    print(completed_count)
    print(type(completed_count))

    # Create a pie chart
    labels = ['Completed Orders', 'Pending Orders']
    sizes = [completed_count, pending_count]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode 1st slice

    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90, )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer


def generate_monthly_orders_bar_graph(df):
    # Convert 'order_date' column to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Extract month from 'order_date' column
    df['order_month'] = df['order_date'].dt.month_name()

    # Count the number of orders in each month
    monthly_orders = df['order_month'].value_counts().sort_index()

    # Create bar graph
    plt.figure(figsize=(10, 8))
    monthly_orders.plot(kind='bar', color='skyblue')
    plt.title('Orders in Months')
    plt.xlabel('Month')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer


def generate_material_pie_chart(df):
    # Count occurrences of each material
    material_counts = df['material_name'].value_counts()

    # Create pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(material_counts, labels=material_counts.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Various Raw Materials')

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer

def generate_supplier_pie_chart(df):
    # Count occurrences of each type
    type_counts = df['type'].value_counts()

    # Create pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Supplier Types')

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer
