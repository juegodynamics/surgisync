import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Toolbar from '@mui/material/Toolbar';
import texture from './darkParchTexture.png';

export default function Main({children}: {children: React.ReactNode}) {
    return (
        <Stack
            direction="row"
            justifyContent="center"
            alignItems="center"
            sx={{width: '100%', overflowY: 'auto', overflowX: 'visible', pt: 4}}
        >
            <Stack
                component="main"
                sx={{
                    width: 'min(1200px, 90vw)',
                    height: '100vh',
                }}
            >
                <Toolbar />
                <Paper
                    sx={{
                        p: 3,
                        borderRadius: '20px',
                    }}
                >
                    {children}
                </Paper>
            </Stack>
        </Stack>
    );
}
