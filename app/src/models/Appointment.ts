export interface Reference {
    reference: string;
    type: string; // should be ResourceType
}

export interface Coding {
    system: string;
    code: string;
    display: string;
}

export interface CodeableConcept {
    text: string;
    coding: Coding[];
}

export interface Appointment {
    id?: string;
    resourceType: 'Appointment';
    status:
        | 'proposed'
        | 'pending'
        | 'booked'
        | 'arrived'
        | 'fulfilled'
        | 'cancelled'
        | 'noshow'
        | 'entered-in-error'
        | 'checked-in'
        | 'waitlist';
    subject: Reference;
    participant: AppointmentParticipant[];
    start: Date;
    end: Date;
}

export interface AppointmentParticipant {
    actor: Reference;
    required: boolean;
    status: 'accepted' | 'declined' | 'tentative' | 'needs-action';
    type: CodeableConcept[];
}

export interface Patient {
    id: string;
    name: [
        {
            family: string;
            given: string[];
        }
    ];
}
