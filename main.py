import logging
from scrapper.linkedin import ScraperLinkedIn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
email = 'tu_email'
password = 'tu_clave'

urls = [
        'https://www.linkedin.com/in/sergio-cabrera-878766239/',
        'https://www.linkedin.com/in/edgardo-fede-gonzalez',
        'https://www.linkedin.com/in/franco-ahumada',
        'https://www.linkedin.com/in/alfredo-carini-498041127/',
        'https://www.linkedin.com/in/cristian-gerard',
        'https://www.linkedin.com/in/ema-lovecchio',
        'https://www.linkedin.com/in/mauro-u-047a44b7',
        'https://www.linkedin.com/in/gerardosabetta',
        'https://www.linkedin.com/in/jeronimo-ferreira-573a7477/',
        'https://www.linkedin.com/in/sebastian-j-peinador-6751a9171',
        'https://www.linkedin.com/in/goblinslay3r',
        'https://www.linkedin.com/in/carlos-galindez-78737613b',
        'https://www.linkedin.com/in/cnmendez',
        'https://www.linkedin.com/in/arielanonis/',
        'https://www.linkedin.com/in/daniel-lezcano',
        'https://www.linkedin.com/in/carlos-cesar-ramirez-c-54ba33174',
        'https://www.linkedin.com/in/matias-m-bb078b238/',
        'https://www.linkedin.com/in/nicolas-perez-77176389',
        'https://www.linkedin.com/in/juan-lucas-armendares-10042850/',
        'https://www.linkedin.com/in/ricardo-e-quezada-s%C3%A1nchez-219a2052/',
        'https://www.linkedin.com/in/cristianchavezz/',
        'https://www.linkedin.com/in/matias-ezequiel-escobar/',
        'https://www.linkedin.com/in/sebastian-landeo-c-4260011b9',
        'https://www.linkedin.com/in/cristian-miranda-velasquez',
        'https://www.linkedin.com/in/tom-gior/',
        'https://www.linkedin.com/in/leonardo-morales-erezuma',
        'https://www.linkedin.com/in/ivandelgadilloz/',
        'https://www.linkedin.com/in/pablo-adrian-del-barco-6291a227',
        'https://www.linkedin.com/in/eliud-muniz/',
        'https://www.linkedin.com/in/baguilar25/',
        'https://www.linkedin.com/in/diegoandrescastro',
        'https://www.linkedin.com/in/roldancapponimaximiliano',
        'https://www.linkedin.com/in/agustin-albornoz-wenner-971a2b159',
        'https://www.linkedin.com/in/erwin-sander',
        'https://www.linkedin.com/in/juan-alberto-flores-quiroga-48387126',
        'https://www.linkedin.com/in/lucas-gallina',
        'https://www.linkedin.com/in/jonathan-guevara-454b2253/',
        'https://www.linkedin.com/in/luccamusomecci/',
        'https://www.linkedin.com/in/emanuel-damico/',
        'https://www.linkedin.com/in/uriel-lorenzo',
        'https://www.linkedin.com/in/fede-masin',
        'https://www.linkedin.com/in/aspano/',
        'https://www.linkedin.com/in/alan-rios-18b77a237/',
        'https://www.linkedin.com/in/sol-al',
        'https://www.linkedin.com/in/facundo-majda-678750252/',
        'https://www.linkedin.com/in/luis-enrique-rodriguez-640566238/',
        'https://www.linkedin.com/in/daniel-leal-716918241',
        'https://www.linkedin.com/in/emanuel-lopez-del-castillo-04b162107',
        'https://www.linkedin.com/in/egimenez',
        'https://www.linkedin.com/in/joaquín-rodriguez-llaneza',
        'https://www.linkedin.com/in/jean-reveiz-58261923a',
        'https://www.linkedin.com/in/c3sar-b4rraza',
        'https://www.linkedin.com/in/unaurl',
        'https://www.linkedin.com/in/matías-pacheco/',
        'https://www.linkedin.com/in/hern%C3%A1n-m%C3%A1rquez',
        'https://www.linkedin.com/in/luciano-poli-97a86123a/',
        'https://www.linkedin.com/in/cusimatias',
        'https://www.linkedin.com/in/brandom-louis-sipan-34a2b81b9',
        'https://www.linkedin.com/in/marianela-sanchez-57732a286',
        'https://www.linkedin.com/in/agustinamisamolina-571473264',
        'https://www.linkedin.com/in/juan-s-solis/',
        'https://www.linkedin.com/in/c-r-navarro88/',
        'https://www.linkedin.com/in/joaquin-martinez-31abb793/',
    ]
try:
    scraper = ScraperLinkedIn(email, password)
    scraper.login()
    scraper.follow_urls(urls)
    scraper.close()
except Exception as e:
    logger.error(f'Error durante el inicio de sesión: {e}')


