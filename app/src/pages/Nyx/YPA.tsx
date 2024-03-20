import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Latex from 'react-latex';

export const YPAWord = ({children}: {children: React.ReactNode}) => (
  <Stack
    spacing={-2}
    direction="row"
    justifyContent="center"
    alignItems="center"
    sx={{width: '100%'}}
  >
    {children}
  </Stack>
);

export const YPASyllable = ({children}: {children: React.ReactNode}) => (
  <Stack
    spacing={-0.75}
    direction="column"
    justifyContent="center"
    alignItems="center"
  >
    {children}
  </Stack>
);

export const Vocal = ({vals}: {vals?: Array<number>}) =>
  vals?.length === 2 ? (
    <Typography>
      <Latex>{`$« \\frac{${vals[0]}}{${vals[1]}} »$`}</Latex>
    </Typography>
  ) : vals?.length === 4 ? (
    <Typography>
      <Latex>{`$« \\frac{${vals[0]}}{${vals[1]}}, \\frac{${vals[2]}}{${vals[3]}} »$`}</Latex>
    </Typography>
  ) : (
    <Typography>
      <Latex>{`$«\\ 𝕀\\ »$`}</Latex>
    </Typography>
  );

export const NoVocal = () => (
  <Typography>
    <Latex>{`$«\\ ∅\\ »$`}</Latex>
  </Typography>
);

export const Aurora = ({
  form,
  motion,
  color,
}: {
  form: string;
  motion: string;
  color: string;
}) => (
  <Typography fontSize="18pt">
    <Latex>{`$${form}^${motion}_{\\raisebox{0.5pt}{${color}}}$`}</Latex>
  </Typography>
);

export const Speech = ({children}: {children: React.ReactNode}) => (
  <Typography fontFamily="Noto Serif" fontSize="16pt" pt="2pt" pb="1pt">
    {children}
  </Typography>
);
