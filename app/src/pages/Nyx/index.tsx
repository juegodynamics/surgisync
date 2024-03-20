import Stack from '@mui/material/Stack';

import {Nyx1} from './sections';
import {Centered} from './Layout';

export default function Nyx() {
  return (
    <Centered>
      <Stack direction="column" sx={{width: '100%'}}>
        <Nyx1 />
      </Stack>
    </Centered>
  );
}
