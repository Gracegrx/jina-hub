from .. import AudioReader


def test_1():
    import librosa
    audio_file_path = librosa.util.example_audio_file()

    crafter = AudioReader()
    crafted_docs = crafter.craft([audio_file_path, audio_file-path], 0)

    assert len(crafted_docs) == 2
    signal = crafted_docs[0]['blob']
    assert signal.shape == (2, 1355168)

    signal = crafted_docs[1]['blob']
    assert signal.shape == (2, 1355168)
