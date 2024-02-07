# Basilar Membrane filter coefficients
COMPRESS_BASILAR_MEMBRANE_COEFS = {
    "24000": {
        "b": [0.09510798340249643, 0.09510798340249643],
        "a": [1.0, -0.8097840331950071],
    }
}
# Middle ear filter coefficients
MIDDLE_EAR_COEF = {
    "24000": {
        "butterworth_low_pass": [0.4341737512063021, 0.4341737512063021],
        "low_pass": [1.0, -0.13165249758739583],
        "butterworth_high_pass": [
            0.9372603902698923,
            -1.8745207805397845,
            0.9372603902698923,
        ],
        "high_pass": [1.0, -1.8705806407352794, 0.8784609203442912],
    }
}
# Resample filter coefficients
RESAMPLE_COEFS = {
    "22050": {
        "a": [
            1.0,
            6.563229198721187,
            18.505433817865256,
            29.05506150301662,
            27.433674675654423,
            15.576261643609874,
            4.923968595144289,
            0.6685242529240554,
        ],
        "b": [
            0.8176333242499695,
            5.694267965735418,
            17.024770717918447,
            28.32640483556404,
            28.32640483556404,
            17.024770717918447,
            5.694267965735419,
            0.8176333242499697,
        ],
    },
    "24000": {
        "a": [
            1.0,
            5.657986938256279,
            14.00815896651005,
            19.634707135261287,
            16.803741671162324,
            8.771318394792921,
            2.5835900814553923,
            0.3310596846351593,
        ],
        "b": [
            0.5753778624919913,
            3.8728648973844546,
            11.32098778566558,
            18.626050890494696,
            18.626050890494696,
            11.320987785665578,
            3.872864897384454,
            0.5753778624919911,
        ],
    },
    "44100": {
        "a": [
            1.0,
            -0.07081207237077872,
            1.2647594875422048,
            0.2132405823253818,
            0.4820212559269799,
            0.13421541556794442,
            0.06248563152819375,
            0.010693174482029118,
        ],
        "b": [
            0.10526806659004136,
            0.2673828276910548,
            0.5089236138475818,
            0.6667272293722993,
            0.6667272293722992,
            0.5089236138475817,
            0.2673828276910549,
            0.1052680665900414,
        ],
    },
}

DELAY_COEFS = [
    0,
    50,
    92,
    127,
    157,
    183,
    205,
    225,
    242,
    256,
    267,
    275,
    283,
    291,
    299,
    305,
    311,
    316,
    320,
    325,
    329,
    332,
    335,
    338,
    340,
    341,
    342,
    344,
    344,
    345,
    346,
    347,
]
