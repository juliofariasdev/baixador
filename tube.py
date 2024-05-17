from time import sleep
from pytube import YouTube as yt
from tkinter.filedialog import askdirectory
import flet as ft


def main(page: ft.page):
    def baixar(e):
        pass
        page.window_minimized = True
        page.update()
        sleep(1)

        path = askdirectory(title='Selecione uma pasta para baixar o video')
        sleep(1)
        page.window_maximized = True
        page.update()
        url = entrada.value
        video = yt(url)
        video.streams.order_by('resolution').first().download(output_path=path)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    entrada = ft.TextField(label='link do vídeo', width=300)
    button = ft.ElevatedButton(text='baixar',on_click=baixar)
    page.add(
        ft.Row(
            [
                entrada
            ],
            ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        ft.Row(
            [
                button
            ],
            ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)