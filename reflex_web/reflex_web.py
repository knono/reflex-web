import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size
from reflex_web.views.navbar import navbar
from reflex_web.views.header import header
from reflex_web.views.spool import spool
from reflex_web.views.footer import footer



def index()  -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                spool(),
                footer(),
                width="100%",
                spacing=Size.VERY_BIG.value
            )
        )
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE

)

app.add_page(
    index,
    title="El laberinto del minutauro",
    description="Web para trastear con Reflex"
)
app.compile()
