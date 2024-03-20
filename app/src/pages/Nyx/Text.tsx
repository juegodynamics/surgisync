import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';

export const Section = ({children}: {children: React.ReactNode}) => (
  <Typography variant="h1">{children}</Typography>
);
export const Subsection = ({children}: {children: React.ReactNode}) => (
  <Typography variant="h2">{children}</Typography>
);
export const Subsubsection = ({children}: {children: React.ReactNode}) => (
  <Typography variant="h3">{children}</Typography>
);
export const Body = ({
  children,
  sx,
}: {
  children: React.ReactNode;
  sx?: Parameters<typeof Typography>[0]['sx'];
}) => (
  <Typography variant="body1" sx={sx}>
    {children}
  </Typography>
);
