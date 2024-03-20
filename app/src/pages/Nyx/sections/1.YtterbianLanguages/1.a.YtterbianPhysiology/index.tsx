import {Subsection, Body} from 'pages/Nyx/Text';
import {
    YPAWord,
    YPASyllable,
    Vocal,
    NoVocal,
    Aurora,
    Speech,
} from 'pages/Nyx/YPA';
import {Nyx1ai} from './1.a.i.AnatomicalReview';

export function Nyx1a() {
    return (
        <>
            <Subsection>{`Ytterbian Physiology`}</Subsection>
            <Body>
                {`Ytterbian physiology diverges markedly from that of humans, shaping their unique linguistic system. While they have an oral cavity and sound-producing cords like ours, their extraterrestrial body structures lead to them generating sounds unrecognizeable in human languages. Their trifurcated vibrational cords allow for simultaneous multitonal production. Additionally, Ytterbians can emit aurorae, introducing a vast luminous communicative dimension. Possessing a singular organ and cortex for both visual and auditory perception, all Ytterbians experience audiovisual synesthesia. Consequently, their languages often equate aurorae production with additional concurrent phonemes. An example in YPA (Ytterbian Photophonetic Alphabet) for "Nice to meet you" in Nyx illustrates this complexity:`}
            </Body>
            <YPAWord>
                <YPASyllable>
                    <Vocal vals={[6, 5, 3, 2]} />
                    <Speech>ʢѩᴛ͡ß</Speech>
                    <Aurora form="񇨓" motion="񋚣" color="񍰱" />
                </YPASyllable>
                <YPASyllable>
                    <Vocal />
                    <Speech>ζꚗȵθ</Speech>
                    <Aurora form="񉸤" motion="񇅤" color="񍼱" />
                </YPASyllable>
                <YPASyllable>
                    <NoVocal />
                    <Speech>ʞҩɾt</Speech>
                    <Aurora form="񇣳" motion="񋔣" color="񍬑" />
                </YPASyllable>
            </YPAWord>
            {/* <Nyx1ai /> */}
        </>
    );
}
