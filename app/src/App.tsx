import CssBaseline from '@mui/material/CssBaseline';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Page from './nav';
import Scheduling from './services/scheduling';

const PRIMARY = '#ED80BD';
const SECONDARY = '#6dc3f5';

// const textPadding = {
//   paddingLeft: '200px',
//   paddingRight: '200px',
// };

const theme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: PRIMARY,
        },
        secondary: {
            main: SECONDARY,
        },
        info: {
            main: '#101010',
        },
        background: {
            default: '#262626',
        },
    },
    typography: {
        fontFamily: [
            'SuttonSignWritingOneD',
            '-apple-system',
            'BlinkMacSystemFont',
            '"Segoe UI"',
            'Roboto',
            '"Helvetica Neue"',
            'Arial',
            'sans-serif',
            '"Apple Color Emoji"',
            '"Segoe UI Emoji"',
            '"Segoe UI Symbol"',
        ].join(','),
        body1: {
            textIndent: '16pt',
            textAlign: 'justify',
            textJustify: 'inter-word',
            // ...textPadding,
        },
        h1: {
            textIndent: '0pt',
            fontSize: '44pt',
            fontWeight: 800,
            color: '#BFBFBF',
            borderBottom: `1px ${SECONDARY} solid`,
            paddingBottom: '10pt',
            marginBottom: '10pt',
            // ...textPadding,
        },
        h2: {
            textIndent: '0pt',
            fontSize: '24pt',
            fontWeight: 'bolder',
            color: '#ED80BD',
            marginTop: '5pt',
            marginBottom: '5pt',
            // ...textPadding,
        },
        h3: {
            textIndent: '0pt',
            fontSize: '18pt',
            marginTop: '5pt',
            marginBottom: '5pt',
            color: '#f545a6',
            // ...textPadding,
        },
    },
});

function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Scheduling />
        </ThemeProvider>
    );
}

export default App;
