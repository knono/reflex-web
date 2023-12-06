import reflex as rx
import reflex_web.constants as constants
import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size, TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "El planeta perdido.",
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="nono_181x189.png",
                alt="Avatar de nono.",
                width="8em",
                height="8em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("Mi libretilla."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    rx.link(
                    "Hecho en reflex...",
                    href=constants.REFLEX_URL,
                    is_external=True,
                    color=TextColor.TERTIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                    ),
                    "¡",
                    rx.span(
                        "Qué maravilla",
                        color=TextColor.QUATERNARY.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!"
                ),
                align_items="start"
            ),
            flex_direction=["column","row","row","row","row"]
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )