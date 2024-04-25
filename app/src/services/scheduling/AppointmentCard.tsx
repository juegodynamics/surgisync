import dayjs from 'dayjs';
import Stack from '@mui/material/Stack';
import MenuItem from '@mui/material/MenuItem';
import Typography from '@mui/material/Typography';
import Select from '@mui/material/Select';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import {DemoItem} from '@mui/x-date-pickers/internals/demo';
import {AdapterDayjs} from '@mui/x-date-pickers/AdapterDayjs';
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider';
import {DateTimeField} from '@mui/x-date-pickers/DateTimeField';
import {Appointment, Patient} from 'models/Appointment';
import {Button, CardActions} from '@mui/material';

const getPatientName = (patient?: Patient) =>
    patient
        ? ((name: Patient['name'][number]) =>
              [name.given.join(' '), name.family].join(' '))(patient.name[0])
        : '';

export const AppointmentCard = ({
    patients,
    appointment,
    saveAppointment,
    updateAppointment,
    deleteAppointment,
}: {
    patients: Patient[];
    appointment: Appointment;
    saveAppointment: (appointment: Appointment) => void;
    updateAppointment: (appointment: Appointment) => void;
    deleteAppointment: (appointmentId: string) => void;
}) => {
    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Card>
                <CardContent>
                    <Stack spacing={2}>
                        <Typography variant="h2">{`Appointment ${
                            appointment.id || '(unsaved)'
                        }`}</Typography>

                        <Select
                            value={appointment.subject.reference}
                            label="Patient"
                            renderValue={(id) =>
                                getPatientName(
                                    patients.find(
                                        (patient) => patient.id === id
                                    )
                                )
                            }
                            onChange={(event) => {
                                updateAppointment({
                                    ...appointment,
                                    subject: {
                                        reference: event.target.value,
                                        type: 'Patient',
                                    },
                                });
                            }}
                        >
                            {patients.map((patient) => (
                                <MenuItem key={patient.id} value={patient.id}>
                                    {getPatientName(patient)}
                                </MenuItem>
                            ))}
                        </Select>

                        <DemoItem label="Start Date Time">
                            <DateTimeField
                                value={dayjs(appointment.start)}
                                onChange={(newStartDateTime) => {
                                    if (newStartDateTime) {
                                        updateAppointment({
                                            ...appointment,
                                            start: newStartDateTime.toDate(),
                                            end: newStartDateTime.isAfter(
                                                appointment.end
                                            )
                                                ? newStartDateTime.toDate()
                                                : appointment.end,
                                        });
                                    }

                                    return;
                                }}
                            />
                        </DemoItem>
                        <DemoItem label="End Date Time">
                            <DateTimeField
                                value={dayjs(appointment.end)}
                                onChange={(newEndDateTime) => {
                                    if (newEndDateTime) {
                                        updateAppointment({
                                            ...appointment,
                                            end: newEndDateTime.toDate(),
                                            start: newEndDateTime.isBefore(
                                                appointment.start
                                            )
                                                ? newEndDateTime.toDate()
                                                : appointment.start,
                                        });
                                    }
                                    return;
                                }}
                            />
                        </DemoItem>
                    </Stack>
                </CardContent>
                <CardActions>
                    <Button onClick={() => saveAppointment(appointment)}>
                        Save
                    </Button>
                    <Button
                        onClick={() =>
                            appointment.id && deleteAppointment(appointment.id)
                        }
                    >
                        Delete
                    </Button>
                </CardActions>
            </Card>
        </LocalizationProvider>
    );
};
