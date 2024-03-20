import Stack from '@mui/material/Stack';

export const Centered = ({
  children,
  sx,
}: {
  children: React.ReactNode;
  sx?: Parameters<typeof Stack>[0]['sx'];
}) => (
  <Stack
    spacing={0}
    direction="row"
    justifyContent="center"
    alignItems="center"
    sx={sx ? sx : {width: '100%'}}
  >
    {children}
  </Stack>
);
