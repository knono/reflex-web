import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size,TextColor

def spool() -> rx.Component:
    return rx.box(
        rx.vstack(
            # rx.span(
            #     rx.text(
            #         "Docker: ",
            #         rx.span(
            #                 "Qué maravilla",
            #                 color=TextColor.ACCENT.value,
            #             ),
            #         class_name="title"
            #     ),
            #     rx.span(
            #         "Prueba"
            #     ),
            #     class_name="nes-container is-rounded is-dark with-title",
            #     align_items="start",
            #     width="100%"
            # ),
            rx.span(
                rx.text(
                    "Docker: ",
                    rx.span(
                            "Manage Docker as a non-root user",
                            color=TextColor.ACCENT.value,
                        ),
                    class_name="title"
                ),
                rx.span(
                    "To run Docker without root privileges:",
                    rx.code_block(
"""# 1. Create the docker group
sudo groupadd docker
# 2. Add your user to the docker group.
sudo usermod -aG docker $USER
# 3. Log out and log back in so that your group membership
# is re-evaluated. You can also run the following command
# to activate the changes to groups:
newgrp docker
# 4. Check permissions or run next step.
sudo chown -R "$USER":"$USER" /home/"$USER"/.docker
sudo chmod -R g+rwx "$HOME/.docker" """,
                        language="bash",
                        #show_line_numbers=True,
                        theme='dark'
                    ),
                ),
                class_name="nes-container is-rounded is-dark with-title",
                align_items="start",
                width="100%"
            ),
            rx.span(
                rx.text(
                    "Docker: ",
                    rx.span(
                            "To start on boot with systemd",
                            color=TextColor.ACCENT.value,
                        ),
                    class_name="title"
                ),
                rx.span(
                    """ To automatically start Docker and containerd on boot for 
                    other Linux distributions using systemd, run the following commands: """,
                    rx.code_block(
"""sudo systemctl enable docker.service
sudo systemctl enable containerd.service""",
                        language="bash",
                        #show_line_numbers=True,
                        theme='dark'
                    ),
                    "To stop this behavior, use disable instead.",
                    rx.code_block(
"""sudo systemctl disable docker.service
sudo systemctl disable containerd.service""",
                        language="bash",
                        #show_line_numbers=True,
                        theme='dark'
                    ),
                ),
                class_name="nes-container is-rounded is-dark with-title",
                align_items="start",
                width="100%"
            ),
            rx.span(
                rx.text(
                    "Docker: ",
                    rx.span(
                            "buildx",
                            color=TextColor.ACCENT.value,
                        ),
                    class_name="title"
                ),
                rx.span(
                    """ Steps: """,
                    rx.code_block(
"""docker buildx create --name ourbuilder
docker buildx create use ourbuilder
docker buildx build --platform linux/amd64 -t mothur_v1_48:latest . --load""",
                        language="bash",
                        #show_line_numbers=True,
                        theme='dark'
                    ),
                    "Dockerfile. (the design was quite simple)",
                    rx.code_block(
"""FROM ubuntu:23.04

RUN apt-get update
RUN apt-get install -y wget mothur && rm -rf /var/lib/apt/lists/*""",
                        language="docker",
                        show_line_numbers=True,
                        theme='dark'
                    ),
                ),
                class_name="nes-container is-rounded is-dark with-title",
                align_items="start",
                width="100%"
            ),
        ),
        padding_top=Size.MEDIUM.value,
        style=styles.max_width_style
    )