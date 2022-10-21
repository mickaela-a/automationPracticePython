from behave import then
from features.page_objects.basePage import element_displayed, get_element_text
from features.page_objects.product_page import BOTON_ADD_TO_CART, DETALLE_PRODUCTO, NOMBRE_PRODUCTO, PRECIO_PRODUCTO


@then('product details shown')
def see_the_product_details(context):
    title_displayed = element_displayed(context, NOMBRE_PRODUCTO)
    assert title_displayed == True
    product_name_text = get_element_text(context, NOMBRE_PRODUCTO)
    assert product_name_text == 'Samsung galaxy s6'
    price_displayed = element_displayed(context, PRECIO_PRODUCTO)
    assert price_displayed == True
    product_price_text = get_element_text(context, PRECIO_PRODUCTO)
    assert product_price_text == '$360 *includes tax'
    descripcion_displayed = element_displayed(context, DETALLE_PRODUCTO)
    assert descripcion_displayed == True
    product_detail_text = get_element_text(context, DETALLE_PRODUCTO)
    assert product_detail_text == 'The Samsung Galaxy S6 is powered by 1.5GHz octa-core Samsung Exynos 7420 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage cannot be expanded.'
    add_to_cart_boton_displayed = element_displayed(context, BOTON_ADD_TO_CART)
    assert add_to_cart_boton_displayed == True
    