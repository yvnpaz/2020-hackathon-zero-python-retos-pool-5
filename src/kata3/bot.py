import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Geeks!")

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text("Ayudame!")

def mayus(update, context):
    may = update.message.text.upper()
    update.message.reply_text(may)

def alreves(update, context):
    """Repite el mensaje del usuario."""
    wordReverse = update.message.text[::-1]
    update.message.reply_text(wordReverse)

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater(NEW_TOKEN, use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    mayus_handler = CommandHandler('mayus', mayus)
    alreves_handler = CommandHandler('alreves', alreves)

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    #
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(mayus_handler)
    dp.add_handler(alreves_handler)

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    updater.idle()
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
