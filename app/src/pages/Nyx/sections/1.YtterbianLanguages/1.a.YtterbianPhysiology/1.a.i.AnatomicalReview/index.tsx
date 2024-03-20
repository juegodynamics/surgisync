import {Body, Subsubsection} from 'pages/Nyx/Text';
import {YtterbianAnatomy} from './YtterbianAnatomy';
import {Centered} from 'pages/Nyx/Layout';

export function Nyx1ai() {
    return (
        <>
            <Subsubsection>{`Anatomical Review`}</Subsubsection>
            <Body>{`The primary structures involved in language production are as follows:`}</Body>
            <Centered>
                <YtterbianAnatomy />
            </Centered>
        </>
    );
}
