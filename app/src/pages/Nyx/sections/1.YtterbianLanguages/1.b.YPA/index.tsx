import PlayArrow from '@mui/icons-material/PlayArrow';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import {Body, Subsection} from 'pages/Nyx/Text';
import React from 'react';
import {
    ArticulationManner,
    ArticulationPlace,
    consonantAudio,
} from './consonants';
import {useTheme} from '@mui/material';

const Play = ({
    src,
    isSelected,
    altLetter,
    onMouseOver,
    onMouseOut,
    ...props
}: {src: string; isSelected?: boolean; altLetter?: string} & Parameters<
    typeof IconButton
>[0]) => {
    const [isPlaying, setIsPlaying] = React.useState(false);
    const [isHover, setIsHover] = React.useState(false);

    const ref = React.useRef<HTMLMediaElement>(null);

    if (ref.current) isPlaying ? ref.current.play() : ref.current.pause();

    React.useEffect(() => {
        if (!isPlaying && ref.current) {
            ref.current.currentTime = 0;
        }
    }, [isPlaying]);

    React.useEffect(() => {
        if (isSelected && ref.current) {
            ref.current.currentTime = 0;
            setIsPlaying(true);
        }
    }, [isSelected, isPlaying, altLetter]);

    return (
        <Box sx={{width: '100%'}}>
            <IconButton
                onClick={() => setIsPlaying(true)}
                size="small"
                disabled={isPlaying}
                onMouseOver={(e) => {
                    setIsHover(true);
                    onMouseOver?.(e);
                }}
                onMouseOut={(e) => {
                    setIsHover(false);
                    onMouseOut?.(e);
                }}
                {...((isHover || altLetter) && {color: 'primary'})}
                {...(altLetter && {sx: {fontSize: '1.3rem'}})}
                {...props}
            >
                {altLetter || <PlayArrow />}
                <audio
                    src={src}
                    ref={ref}
                    onEnded={() => setIsPlaying(false)}
                />
            </IconButton>
        </Box>
    );
};

const ROW_SELECTORS: Record<string, number> = {
    Digit1: 1,
    Digit2: 2,
    Digit3: 3,
    Digit4: 4,
    Digit5: 5,
    Digit6: 6,
    Digit7: 7,
    Digit8: 8,
    Digit9: 9,
    Digit0: 0,
};

const COLUMN_SELECTORS: Record<string, number> = {
    KeyA: 1,
    KeyS: 2,
    KeyD: 3,
    KeyF: 4,
    KeyG: 5,
    KeyH: 6,
    KeyJ: 7,
    KeyK: 8,
    KeyL: 9,
};

const COLUMN_DISPLAYERS: Record<number, string> = {
    1: 'a',
    2: 's',
    3: 'd',
    4: 'f',
    5: 'g',
    6: 'h',
    7: 'j',
    8: 'k',
    9: 'l',
};

const ConsonantTable = () => {
    const places: ArticulationPlace[] = Object.keys(
        ArticulationPlace
    ) as ArticulationPlace[];
    const manners: ArticulationManner[] = Object.keys(
        ArticulationManner
    ) as ArticulationManner[];

    const [focusedConsonant, setFocusedConsonant] = React.useState<{
        place: ArticulationPlace;
        manner: ArticulationManner;
    } | null>(null);

    const theme = useTheme();

    const [focusedRow, setFocusedRow] = React.useState<number>(0);
    const [focusedColumn, setFocusedColumn] = React.useState<number>(0);

    const handleKeyPress = React.useCallback<(ev: KeyboardEvent) => void>(
        ({code, shiftKey}) => {
            if (Object.keys(ROW_SELECTORS).includes(code)) {
                setFocusedRow((shiftKey ? 10 : 0) + ROW_SELECTORS[code]);
            }
            if (Object.keys(COLUMN_SELECTORS).includes(code)) {
                setFocusedColumn(COLUMN_SELECTORS[code]);
            }
        },
        [setFocusedRow, setFocusedColumn]
    );

    const handleKeyRaise = React.useCallback<(ev: KeyboardEvent) => void>(
        ({code, shiftKey}) => {
            setFocusedRow((priorFocusedRow) => {
                if (
                    Object.keys(ROW_SELECTORS).includes(code) &&
                    priorFocusedRow ===
                        (shiftKey ? 10 : 0) + ROW_SELECTORS[code]
                ) {
                    return 0;
                }
                return priorFocusedRow;
            });
            setFocusedColumn((priorFocusedColumn) => {
                if (
                    Object.keys(COLUMN_SELECTORS).includes(code) &&
                    priorFocusedColumn === COLUMN_SELECTORS[code]
                ) {
                    return 0;
                }
                return priorFocusedColumn;
            });
        },
        [setFocusedRow, setFocusedColumn]
    );

    React.useEffect(() => {
        console.log({focusedRow, focusedColumn});
    }, [focusedRow, focusedColumn]);

    React.useEffect(() => {
        window.addEventListener('keydown', handleKeyPress);
        window.addEventListener('keyup', handleKeyRaise);
        return () => {
            window.removeEventListener('keydown', handleKeyPress);
            window.removeEventListener('keyup', handleKeyRaise);
        };
    }, [handleKeyPress, handleKeyRaise]);

    return (
        <Box p={2}>
            <TableContainer component={Paper}>
                <Table size="small">
                    <TableHead>
                        <TableRow>
                            <TableCell></TableCell>
                            {places.map((place, placeIndex) => (
                                <TableCell
                                    key={placeIndex}
                                    align="center"
                                    {...(focusedConsonant?.place === place && {
                                        sx: {
                                            color: theme.palette.primary.main,
                                        },
                                    })}
                                >
                                    {place}
                                </TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {manners.map((manner, mannerIndex) => {
                            const isFocusedRow = focusedRow - 1 === mannerIndex;
                            return (
                                <TableRow
                                    key={mannerIndex}
                                    {...(isFocusedRow && {
                                        sx: {
                                            background:
                                                theme.palette.background.paper,
                                        },
                                    })}
                                >
                                    <TableCell
                                        align="left"
                                        component="th"
                                        scope="row"
                                        {...(focusedConsonant?.manner ===
                                            manner && {
                                            sx: {
                                                color: theme.palette.primary
                                                    .main,
                                            },
                                        })}
                                    >
                                        {manner}
                                    </TableCell>
                                    {places.map((place, placeIndex) => {
                                        const src =
                                            consonantAudio?.[manner]?.[place];
                                        const isFocusedColumn =
                                            focusedColumn - 1 === placeIndex;
                                        return (
                                            <TableCell
                                                key={placeIndex}
                                                align="center"
                                                // {...(focusedColumn - 1 === placeIndex && {
                                                //   sx: {backgroundColor: theme.palette.primary.dark},
                                                // })}
                                            >
                                                {src ? (
                                                    <Play
                                                        src={src}
                                                        isSelected={
                                                            isFocusedRow &&
                                                            isFocusedColumn
                                                        }
                                                        onMouseOver={() =>
                                                            setFocusedConsonant(
                                                                {place, manner}
                                                            )
                                                        }
                                                        onMouseOut={() =>
                                                            setFocusedConsonant(
                                                                null
                                                            )
                                                        }
                                                        {...(isFocusedRow && {
                                                            altLetter:
                                                                COLUMN_DISPLAYERS[
                                                                    placeIndex +
                                                                        1
                                                                ],
                                                        })}
                                                    />
                                                ) : null}
                                            </TableCell>
                                        );
                                    })}
                                </TableRow>
                            );
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
};

export function Nyx1b() {
    return (
        <>
            <Subsection>Consonants</Subsection>
            <Body>{`Select any of the consonants below to hear them pronounced. Alternatively, keyboard mode is enabled: hold a 0-9 key to select a row (use Shift to rows 10+), and then press the displayed letter from the second keyboard row.`}</Body>
            <ConsonantTable />
        </>
    );
}
