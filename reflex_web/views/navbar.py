import reflex as rx
import reflex_web.constants as constants
from reflex_web.styles.styles import Size, Color
from reflex_web.components.link_icon import link_icon

def navbar()  -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="nono.png",
                alt="Pequeño robot",
                width=Size.BIG.value,
                height=Size.BIG.value
            ),
            rx.text("El laberinto del Minotauro"),
            rx.spacer(),
            link_icon(
                "linkedin",
                constants.LINKEDIN_URL
            ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom = f"0.05em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )