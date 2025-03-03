import os
import requests
import wikipedia

from io import BytesIO
from PIL import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    """ Object that represents the screen visible to the user """
    def get_image_link(self):
        """ Get the first image link from a Wikipedia page based on user query. """
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        if not query:
            return None # Avoid empty queries

        try:
            # Get the best-matching page title
            search_results = wikipedia.search(query)
            if not search_results:
                return None # No results found

            # Get wikipedia page
            page_title = search_results[0]
            page = wikipedia.page(page_title, auto_suggest=False)

            # Ensure the page has images
            if not page.images:
                return None

            return page.images[0] # Return the first image link

        except wikipedia.exceptions.DisambiguationError as e:
            # Show the user multiple options (return first for now)
            page = wikipedia.page(e.options[0], auto_suggest=False)
            return page.images[0] if page.images else None

        except wikipedia.exceptions.PageError:
            return None # No matching page found

        except requests.exceptions.RequestException:
            return None # Handle network issues

    def download_image(self):
        """ Download and save the Wikipedia image. """
        image_link = self.get_image_link()
        if not image_link:
            return None # No image to download

        try:
            # Download the image
            req = requests.get(image_link, stream=True)
            if req.status_code != 200:
                return None # Invalid response

            # Save the image
            image_path = "files/image.jpeg"
            image_format = image_path.split(".")[-1].lower()
            if image_format in ["jpg", "jpeg", "png"]:
                with open(image_path, "wb") as file:
                    file.write(req.content)
            else:
                image = Image.open(BytesIO(req.content))
                image = image.convert("RGB")  # Convert to RGB (for JPEG)
                image.save(image_path, "JPEG")

            return image_path

        except requests.exceptions.RequestException:
            return None # Handle request errors

    def set_image(self):
        """ Set the downloaded image in the Image widget. """
        image_path = self.download_image()
        default_image_path = "files/default.jpg"
        if image_path:
            # Set the image in the Image widget
            self.manager.current_screen.ids.img.source = image_path
        else:
            self.manager.current_screen.ids.img.source = default_image_path # Fallback image

        self.manager.current_screen.ids.img.reload()


class RootWidget(ScreenManager):
    """
    Object that represents the top-level object in the widget tree,
    which serves as the entry point for the app's UI
    """
    pass


class MainApp(App):
    """ Main object that holds other objects together """
    def build(self):
        return RootWidget()

MainApp().run()
