import reflex as rx
import reflex_web.styles.styles as styles
import reflex_web.constants as constant 
from reflex_web.styles.styles import Size, TextColor

def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "El laberinto del minotauro",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value

            ),
            rx.link(
                "Hecho un finde con ",
                rx.box(class_name="nes-icon is-small heart"),
                " gracias a MoureDev by Brais Moure",
                href=constant.MOUREDEV_URL,
                is_external=True,
                font_size=Size.SMALL.value,
                color=TextColor.TERTIARY.value
            ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            alt="Logo MoureDev. Una letra \"eme\" entre dos corchetes. ",
            class_name="nes-avatar is-rounded is-medium"
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"
    )