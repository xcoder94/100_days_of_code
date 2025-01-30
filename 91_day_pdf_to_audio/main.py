from pypdf import PdfReader
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play


reader = PdfReader('tt_for_Kaz.pdf')
page = reader.pages[0]
extracted_text = page.extract_text()
# print(extracted_text)
load_dotenv()

ELEVENLABS_API_KEY = 'some_key'

client = ElevenLabs(
    api_key = ELEVENLABS_API_KEY
)

audio = client.text_to_speech.convert(
    text=extracted_text,
    voice_id='3EuKHIEZbSzrHGNmdYsx',
    model_id='eleven_multilingual_v2',
    output_format='mp3_44100_128'
)

play(audio)