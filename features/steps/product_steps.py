from behave import then
from features.page_objects.basePage import element_displayed, get_element_text
from features.page_objects.common_constants import DESCRIPCIONSAMSUNGGALAXYS6_STRING, PRECIO_STRING, SAMSUNGGALAXYS6_STRING
from features.page_objects.product_page import BOTON_ADD_TO_CART, FIRSTPRODUCT_DETAIL, FIRSTPRODUCT_PRICE, FIRSTPRODUCT_TITLE


@then('product details are displayed')
def see_the_product_details(context):
    title_displayed = element_displayed(context, FIRSTPRODUCT_TITLE)
    assert title_displayed == True
    product_name_text = get_element_text(context, FIRSTPRODUCT_TITLE)
    assert product_name_text == SAMSUNGGALAXYS6_STRING
    price_displayed = element_displayed(context, FIRSTPRODUCT_PRICE)
    assert price_displayed == True
    product_price_text = get_element_text(context, FIRSTPRODUCT_PRICE)
    assert product_price_text == PRECIO_STRING
    descripcion_displayed = element_displayed(context, FIRSTPRODUCT_DETAIL)
    assert descripcion_displayed == True
    product_detail_text = get_element_text(context, FIRSTPRODUCT_DETAIL)
    assert product_detail_text == DESCRIPCIONSAMSUNGGALAXYS6_STRING
    add_to_cart_boton_displayed = element_displayed(context, BOTON_ADD_TO_CART)
    assert add_to_cart_boton_displayed == True
