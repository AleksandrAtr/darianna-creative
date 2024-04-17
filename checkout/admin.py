from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin configuration for OrderLineItem model.
    """

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for Order model.
    """

    # Display OrderLineItem inline in Order admin page
    inlines = (OrderLineItemAdminInline,)

    # Readonly fields in Order admin page
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    # Fieldsets configuration in Order admin page
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    # List display configuration in Order admin page
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Ordering configuration in Order admin page
    ordering = ('-date',)

# Register Order model with OrderAdmin configuration
admin.site.register(Order, OrderAdmin)
