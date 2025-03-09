import requests
from decouple import config

# version1
# class MediaDownloader:
#     def __init__(self, tmdb_api_key=config('TMDB_API_KEY'), omdb_api_key=config('XUI_ONE_DB_HOST')):
#         """
#         Inicializa la clase con las claves de API necesarias.
#         :param tmdb_api_key: Clave de API para TMDB.
#         :param omdb_api_key: Clave de API para OMDb.
#         """
#         self.tmdb_api_key = tmdb_api_key
#         self.omdb_api_key = omdb_api_key
#         self.tmdb_base_url = "https://api.themoviedb.org/3"
#         self.omdb_base_url = "http://www.omdbapi.com/"
#
#     def search_by_name(self, media_type, query):
#         """
#         Busca una película o serie por nombre en TMDB.
#         :param media_type: 'movie' o 'tv' para especificar el tipo de contenido.
#         :param query: Nombre de la película o serie a buscar.
#         :return: Lista de resultados encontrados.
#         """
#         endpoint = f"{self.tmdb_base_url}/search/{media_type}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "query": query,
#             "language": "es-ES"  # Para obtener resultados en español
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json().get("results", [])
#         else:
#             raise Exception(f"Error al buscar en TMDB: {response.status_code} - {response.text}")
#
#     def get_details_by_id(self, media_type, media_id):
#         """
#         Obtiene detalles de una película o serie por ID en TMDB.
#         :param media_type: 'movie' o 'tv' para especificar el tipo de contenido.
#         :param media_id: ID de la película o serie en TMDB.
#         :return: Detalles completos del contenido.
#         """
#         endpoint = f"{self.tmdb_base_url}/{media_type}/{media_id}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "language": "es-ES"
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception(f"Error al obtener detalles en TMDB: {response.status_code} - {response.text}")
#
#     def get_omdb_details(self, imdb_id):
#         """
#         Obtiene detalles adicionales de una película o serie desde OMDb usando su IMDb ID.
#         :param imdb_id: ID de IMDb de la película o serie.
#         :return: Detalles adicionales desde OMDb.
#         """
#         params = {
#             "apikey": self.omdb_api_key,
#             "i": imdb_id
#         }
#         response = requests.get(self.omdb_base_url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             if data.get("Response") == "True":
#                 return data
#             else:
#                 raise Exception(f"No se encontraron detalles en OMDb: {data.get('Error')}")
#         else:
#             raise Exception(f"Error al obtener detalles en OMDb: {response.status_code} - {response.text}")
#
#     def download_media_info(self, media_type, query_or_id):
#         """
#         Método principal para descargar información completa de una película o serie.
#         Combina datos de TMDB y OMDb.
#         :param media_type: 'movie' o 'tv'.
#         :param query_or_id: Nombre o ID de la película/serie.
#         :return: Diccionario con toda la información combinada.
#         """
#         # Paso 1: Obtener datos de TMDB
#         if isinstance(query_or_id, int):  # Si es un ID
#             tmdb_data = self.get_details_by_id(media_type, query_or_id)
#         else:  # Si es un nombre
#             results = self.search_by_name(media_type, query_or_id)
#             if not results:
#                 raise Exception("No se encontraron resultados en TMDB.")
#             tmdb_data = self.get_details_by_id(media_type, results[0]["id"])  # Tomamos el primer resultado
#
#         # Paso 2: Extraer el IMDb ID de los datos de TMDB
#         imdb_id = tmdb_data.get("imdb_id")
#         if not imdb_id:
#             raise Exception("No se encontró un IMDb ID en los datos de TMDB.")
#
#         # Paso 3: Obtener datos adicionales de OMDb
#         omdb_data = self.get_omdb_details(imdb_id)
#
#         # Paso 4: Combinar datos de TMDB y OMDb
#         combined_data = {
#             "tmdb_data": tmdb_data,
#             "omdb_data": omdb_data
#         }
#         return combined_data


# version2
# class MediaDownloader:
#     def __init__(self, tmdb_api_key=config('TMDB_API_KEY'), omdb_api_key=config('XUI_ONE_DB_HOST')):
#         """
#         Inicializa la clase con las claves de API necesarias.
#         :param tmdb_api_key: Clave de API para TMDB.
#         :param omdb_api_key: Clave de API para OMDb.
#         """
#         self.tmdb_api_key = tmdb_api_key
#         self.omdb_api_key = omdb_api_key
#         self.tmdb_base_url = "https://api.themoviedb.org/3"
#         self.omdb_base_url = "http://www.omdbapi.com/"
#
#     def search_by_name(self, media_type, query):
#         """
#         Busca una película o serie por nombre en TMDB.
#         :param media_type: 'movie' o 'tv' para especificar el tipo de contenido.
#         :param query: Nombre de la película o serie a buscar.
#         :return: Lista de resultados encontrados.
#         """
#         endpoint = f"{self.tmdb_base_url}/search/{media_type}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "query": query,
#             "language": "es-MX"  # Para obtener resultados en español
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json().get("results", [])
#         else:
#             raise Exception(f"Error al buscar en TMDB: {response.status_code} - {response.text}")
#
#     def get_details_by_id(self, media_type, media_id):
#         """
#         Obtiene detalles de una película o serie por ID en TMDB.
#         :param media_type: 'movie' o 'tv'.
#         :param media_id: ID de la película o serie en TMDB.
#         :return: Detalles completos del contenido.
#         """
#         endpoint = f"{self.tmdb_base_url}/{media_type}/{media_id}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "language": "es-MX"
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception(f"Error al obtener detalles en TMDB: {response.status_code} - {response.text}")
#
#     def get_omdb_details(self, imdb_id):
#         """
#         Obtiene detalles adicionales de una película o serie desde OMDb usando su IMDb ID.
#         :param imdb_id: ID de IMDb de la película o serie.
#         :return: Detalles adicionales desde OMDb o un objeto vacío si no se encuentra.
#         """
#         params = {
#             "apikey": self.omdb_api_key,
#             "i": imdb_id
#         }
#         response = requests.get(self.omdb_base_url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             if data.get("Response") == "True":
#                 return data
#             else:
#                 # Si no se encuentran datos en OMDb, retornamos un objeto vacío
#                 return {}
#         else:
#             # Si hay un error en la solicitud, retornamos un objeto vacío
#             return {}
#
#     def download_media_info(self, media_type, query_or_id):
#         """
#         Método principal para descargar información completa de una película o serie.
#         Combina datos de TMDB y OMDb.
#         :param media_type: 'movie' o 'tv'.
#         :param query_or_id: Nombre o ID de la película/serie.
#         :return: Diccionario con toda la información combinada.
#         """
#         # Paso 1: Obtener datos de TMDB
#         try:
#             if isinstance(query_or_id, int):  # Si es un ID
#                 tmdb_data = self.get_details_by_id(media_type, query_or_id)
#             else:  # Si es un nombre
#                 results = self.search_by_name(media_type, query_or_id)
#                 if not results:
#                     return {"error": "No se encontraron resultados en TMDB."}
#                 tmdb_data = self.get_details_by_id(media_type, results[0]["id"])  # Tomamos el primer resultado
#         except Exception as e:
#             return {"error": f"Error al obtener datos de TMDB: {str(e)}"}
#
#         # Paso 2: Extraer el IMDb ID de los datos de TMDB
#         imdb_id = tmdb_data.get("imdb_id")
#         if not imdb_id:
#             # Si no hay IMDb ID, retornamos los datos de TMDB sin datos de OMDb
#             return {"tmdb_data": tmdb_data, "omdb_data": {}}
#
#         # Paso 3: Obtener datos adicionales de OMDb
#         omdb_data = self.get_omdb_details(imdb_id)
#
#         # Paso 4: Combinar datos de TMDB y OMDb
#         combined_data = {
#             "tmdb_data": tmdb_data,
#             "omdb_data": omdb_data
#         }
#         return combined_data


# version3
class MediaDownloader:
    def __init__(self, tmdb_api_key=config('TMDB_API_KEY'), omdb_api_key=config('XUI_ONE_DB_HOST')):
        """
        Inicializa la clase con las claves de API necesarias.
        :param tmdb_api_key: Clave de API para TMDB.
        :param omdb_api_key: Clave de API para OMDb.
        """
        self.tmdb_api_key = tmdb_api_key
        self.omdb_api_key = omdb_api_key
        self.tmdb_base_url = "https://api.themoviedb.org/3"
        self.omdb_base_url = "http://www.omdbapi.com/"

    def search_by_name(self, media_type, query):
        """
        Busca una película o serie por nombre en TMDB.
        :param media_type: 'movie' o 'tv' para especificar el tipo de contenido.
        :param query: Nombre de la película o serie a buscar.
        :return: Lista de resultados encontrados.
        """
        endpoint = f"{self.tmdb_base_url}/search/{media_type}"
        params = {
            "api_key": self.tmdb_api_key,
            "query": query,
            "language": "es-MX",  # Para obtener resultados en español
            "page": 1
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            raise Exception(f"Error al buscar en TMDB: {response.status_code} - {response.text}")

    def get_details_by_id(self, media_type, media_id):
        """
        Obtiene detalles de una película o serie por ID en TMDB.
        :param media_type: 'movie' o 'tv'.
        :param media_id: ID de la película o serie en TMDB.
        :return: Detalles completos del contenido.
        """
        endpoint = f"{self.tmdb_base_url}/{media_type}/{media_id}"
        params = {
            "api_key": self.tmdb_api_key,
            "language": "es-MX"
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener detalles en TMDB: {response.status_code} - {response.text}")

    def get_omdb_details(self, imdb_id):
        """
        Obtiene detalles adicionales de una película o serie desde OMDb usando su IMDb ID.
        :param imdb_id: ID de IMDb de la película o serie.
        :return: Detalles adicionales desde OMDb o un objeto vacío si no se encuentra.
        """
        params = {
            "apikey": self.omdb_api_key,
            "i": imdb_id
        }
        response = requests.get(self.omdb_base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("Response") == "True":
                return data
            else:
                # Si no se encuentran datos en OMDb, retornamos un objeto vacío
                return {}
        else:
            # Si hay un error en la solicitud, retornamos un objeto vacío
            return {}

    def download_media_info(self, media_type, query_or_id):
        """
        Método principal para descargar información completa de una película o serie.
        Combina datos de TMDB y OMDb.
        :param media_type: 'movie' o 'tv'.
        :param query_or_id: Nombre o ID de la película/serie.
        :return: Lista de diccionarios con toda la información combinada.
        """
        results = []

        try:
            if isinstance(query_or_id, int):  # Si es un ID
                tmdb_data = self.get_details_by_id(media_type, query_or_id)
                results.append(tmdb_data)  # Añadimos el único resultado
            else:  # Si es un nombre
                results = self.search_by_name(media_type, query_or_id)  # Obtenemos todos los resultados
        except Exception as e:
            return {"error": f"Error al obtener datos de TMDB: {str(e)}"}

        combined_results = []

        for result in results:
            # Extraer el IMDb ID de los datos de TMDB
            imdb_id = result.get("imdb_id")
            if not imdb_id:
                # Si no hay IMDb ID, agregamos los datos de TMDB sin datos de OMDb
                combined_results.append({"tmdb_data": result, "omdb_data": {}})
                continue

            # Obtener datos adicionales de OMDb
            omdb_data = self.get_omdb_details(imdb_id)

            # Combinar datos de TMDB y OMDb
            combined_results.append({
                "tmdb_data": result,
                "omdb_data": omdb_data
            })

        return combined_results

    # Seasons and episodes
    def get_season_details(self, series_id, season_number):
        """
        Obtiene los detalles de una temporada específica de una serie en TMDB.
        :param series_id: ID de la serie en TMDB.
        :param season_number: Número de la temporada.
        :return: Detalles completos de la temporada.
        """
        endpoint = f"{self.tmdb_base_url}/tv/{series_id}/season/{season_number}"
        params = {
            "api_key": self.tmdb_api_key,
            "language": "es-MX"  # Para obtener resultados en español
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Error al obtener detalles de la temporada en TMDB: {response.status_code} - {response.text}")

    def get_episode_details(self, series_id, season_number, episode_number):
        """
        Obtiene los detalles de un episodio específico dentro de una temporada en TMDB.
        :param series_id: ID de la serie en TMDB.
        :param season_number: Número de la temporada.
        :param episode_number: Número del episodio.
        :return: Detalles completos del episodio.
        """
        endpoint = f"{self.tmdb_base_url}/tv/{series_id}/season/{season_number}/episode/{episode_number}"
        params = {
            "api_key": self.tmdb_api_key,
            "language": "es-MX"  # Para obtener resultados en español
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener detalles del episodio en TMDB: {response.status_code} - "
                            f"{response.text}")

# version4
# class MediaDownloader:
#     def __init__(self, tmdb_api_key=config('TMDB_API_KEY'), omdb_api_key=config('XUI_ONE_DB_HOST')):
#         """
#         Inicializa la clase con las claves de API necesarias.
#         :param tmdb_api_key: Clave de API para TMDB.
#         :param omdb_api_key: Clave de API para OMDb.
#         """
#         self.tmdb_api_key = tmdb_api_key
#         self.omdb_api_key = omdb_api_key
#         self.tmdb_base_url = "https://api.themoviedb.org/3"
#         self.omdb_base_url = "http://www.omdbapi.com/"
#
#     def search_by_name(self, media_type, query):
#         """
#         Busca una película o serie por nombre en TMDB.
#         :param media_type: 'movie' o 'tv'.
#         :param query: Nombre de la película o serie a buscar.
#         :return: Lista de resultados encontrados.
#         """
#         endpoint = f"{self.tmdb_base_url}/search/{media_type}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "query": query,
#             "language": "es-MX", # Para obtener resultados en español
#             "page": 1
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json().get("results", [])
#         else:
#             raise Exception(f"Error al buscar en TMDB: {response.status_code} - {response.text}")
#
#     def get_details_by_id(self, media_type, media_id):
#         """
#         Obtiene detalles de una película o serie por ID en TMDB.
#         :param media_type: 'movie' o 'tv'.
#         :param media_id: ID de la película o serie en TMDB.
#         :return: Detalles completos del contenido.
#         """
#         endpoint = f"{self.tmdb_base_url}/{media_type}/{media_id}"
#         params = {
#             "api_key": self.tmdb_api_key,
#             "language": "es-MX"
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception(f"Error al obtener detalles en TMDB: {response.status_code} - {response.text}")
#
#     def get_omdb_details(self, imdb_id):
#         """
#         Obtiene detalles adicionales de una película o serie desde OMDb usando su IMDb ID.
#         :param imdb_id: ID de IMDb de la película o serie.
#         :return: Detalles adicionales desde OMDb o un objeto vacío si no se encuentra.
#         """
#         params = {
#             "apikey": self.omdb_api_key,
#             "i": imdb_id
#         }
#         response = requests.get(self.omdb_base_url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             if data.get("Response") == "True":
#                 return data
#             else:
#                 # Si no se encuentran datos en OMDb, retornamos un objeto vacío
#                 return {}
#         else:
#             # Si hay un error en la solicitud, retornamos un objeto vacío
#             return {}
#
#     def download_media_info(self, media_type, query_or_id):
#         """
#         Método principal para descargar información completa de una película o serie.
#         Combina datos de TMDB y OMDb.
#         :param media_type: 'movie' o 'tv'.
#         :param query_or_id: Nombre o ID de la película/serie.
#         :return: Lista de diccionarios con toda la información combinada.
#         """
#         results = []
#
#         try:
#             if isinstance(query_or_id, int):  # Si es un ID
#                 tmdb_data = self.get_details_by_id(media_type, query_or_id)
#                 results.append(tmdb_data)  # Añadimos el único resultado
#             else:  # Si es un nombre
#                 initial_results = self.search_by_name(media_type, query_or_id)  # Obtenemos todos los resultados iniciales
#                 for result in initial_results:
#                     # Obtenemos los detalles completos usando el ID de cada resultado
#                     full_tmdb_data = self.get_details_by_id(media_type, result["id"])
#                     results.append(full_tmdb_data)
#         except Exception as e:
#             return {"error": f"Error al obtener datos de TMDB: {str(e)}"}
#
#         combined_results = []
#
#         for result in results[:10]:
#             # Extraer el IMDb ID de los datos de TMDB
#             imdb_id = result.get("imdb_id")
#             if not imdb_id:
#                 # Si no hay IMDb ID, agregamos los datos de TMDB sin datos de OMDb
#                 combined_results.append({"tmdb_data": result, "omdb_data": {}})
#                 continue
#
#             # Obtener datos adicionales de OMDb
#             omdb_data = self.get_omdb_details(imdb_id)
#
#             # Combinar datos de TMDB y OMDb
#             combined_results.append({
#                 "tmdb_data": result,
#                 "omdb_data": omdb_data
#             })
#
#         return {"status": "ok", "results": combined_results}





