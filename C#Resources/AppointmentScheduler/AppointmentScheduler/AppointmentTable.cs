//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace AppointmentScheduler
{
    using System;
    using System.Collections.Generic;
    
    public partial class AppointmentTable
    {
        public int AppointmentID { get; set; }
        public System.TimeSpan AppointmentTime { get; set; }
        public System.DateTime AppointmentDate { get; set; }
        public string AppointmentReason { get; set; }
        public int AdvisorID { get; set; }
        public int StudentID { get; set; }
    }
}
