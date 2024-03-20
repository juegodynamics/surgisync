import {Section, Body} from 'pages/Nyx/Text';
import {Nyx1a} from './1.a.YtterbianPhysiology';
import {Nyx1b} from './1.b.YPA';
import {Box} from '@mui/material';

export function Nyx1() {
    return (
        <>
            <Section>{`Section 1 – Ytterbian Languages`}</Section>
            <Body>
                {`To begin the study of Nyx, first let’s overview the general properties of Ytterbian languages. The next section will then focus on the subset of these properties that apply to Nyx.`}
            </Body>
            <Nyx1a />
            <Nyx1b />
            <Box height="600px" />
        </>
    );
}
